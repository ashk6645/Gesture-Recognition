# Gesture-Recognition
Here is a `README.md` file for your project:

```markdown
# One Finger Drawing with Erase and Pause using OpenCV and MediaPipe

This Python project implements a real-time hand gesture recognition system using OpenCV and MediaPipe. It allows users to draw on a virtual canvas using their index finger, erase the drawing by raising all fingers, and pause drawing by raising two fingers (index and middle). The project captures video from a webcam and processes the video frames to detect hand landmarks and interpret the gestures.

## Features

- **Draw with One Finger**: Draw on the virtual canvas by raising only the index finger.
- **Erase with All Fingers**: Clear the canvas by raising all five fingers.
- **Pause Drawing with Two Fingers**: Pause the drawing action by raising the index and middle fingers.

## Dependencies

- Python 3.x
- OpenCV
- NumPy
- MediaPipe

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/one-finger-drawing.git
   cd one-finger-drawing
   ```

2. **Install Required Packages:**
   Install the necessary Python libraries using pip:
   ```bash
   pip install opencv-python mediapipe numpy
   ```

3. **Run the Script:**
   Run the Python script to start the drawing application:
   ```bash
   python one_finger_drawing.py
   ```

## How It Works

- **Hand Detection**: The program uses MediaPipe to detect hand landmarks in real-time.
- **Gesture Recognition**: Based on the position of the fingers, the program determines the user's gesture (draw, erase, pause).
- **Drawing**: If only the index finger is raised, the program draws a circle on the canvas at the position of the fingertip.
- **Erasing**: If all fingers are raised, the canvas is cleared.
- **Pausing**: If the index and middle fingers are raised, the drawing is paused, and no action is taken.

## Usage

- Start the program, and it will open your webcam feed in a window.
- Use your index finger to draw on the screen.
- Raise all your fingers to clear the canvas.
- Raise your index and middle fingers to pause drawing.
- Press `q` to exit the program.

## Customization

- **Adjust the Drawing Thickness**: Modify the `cv2.circle()` function to change the size of the drawn circles.
- **Change the Canvas Size**: Update the canvas dimensions by modifying the `canvas` variable.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands) - Used for hand tracking and gesture recognition.
- [OpenCV](https://opencv.org/) - Used for real-time video capture and processing.

## Contact

If you have any questions or suggestions, feel free to contact me.

```
