import cv2
import numpy as np
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Initialize OpenCV
cap = cv2.VideoCapture(0)

# Create a blank image for drawing
canvas = np.zeros((480, 640, 3), np.uint8)

def fingers_up(hand_landmarks, w, h):
    """Returns a list indicating whether each finger is up (1) or down (0)"""
    fingers = []

    # Thumb (check if the tip is to the right of the IP joint)
    thumb_tip_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * w
    thumb_ip_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x * w
    fingers.append(1 if thumb_tip_x > thumb_ip_x else 0)

    # For other fingers (check if the tip is above the PIP joint)
    for lm in [mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
               mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP]:
        tip_y = hand_landmarks.landmark[lm].y * h
        pip_y = hand_landmarks.landmark[lm - 2].y * h
        fingers.append(1 if tip_y < pip_y else 0)

    return fingers

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    results = hands.process(rgb_frame)

    # Create a black screen overlay
    overlay = np.zeros((h, w, 3), np.uint8)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Detect if all fingers are up for erasing
            fingers = fingers_up(hand_landmarks, w, h)
            if all(fingers):  # All five fingers are up
                canvas = np.zeros((480, 640, 3), np.uint8)  # Clear the canvas
                cv2.putText(overlay, 'Eraser', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                continue  # Skip the rest to avoid drawing while erasing

            # Detect if two fingers are up for pausing
            if fingers[1] and fingers[2]:  # Index and middle fingers up
                continue  # Pause drawing

            # Extract landmarks for the index finger
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Convert landmarks to pixel coordinates
            index_finger_tip_x = int(index_finger_tip.x * w)
            index_finger_tip_y = int(index_finger_tip.y * h)

            # Draw a circle on the index fingertip
            cv2.circle(frame, (index_finger_tip_x, index_finger_tip_y), 10, (255, 0, 0), -1)

            # Draw on canvas if only the index finger is up
            if fingers[1] and not fingers[2]:  # Only index finger up
                cv2.circle(canvas, (index_finger_tip_x, index_finger_tip_y), 10, (255, 255, 255), -1)
                cv2.putText(overlay, 'Write', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            # Draw the hand landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Merge canvas and frame
    frame = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)
    frame = cv2.addWeighted(frame, 1, overlay, 0.5, 0)

    # Display the result
    cv2.imshow("One Finger Drawing with Erase and Pause", frame)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
