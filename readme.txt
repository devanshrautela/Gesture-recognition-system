This program is a gesture controller developed during a hackathon, securing a position in the top 5. The controller utilizes computer vision and machine learning techniques to interpret hand gestures, providing a hands-free interface for various system controls.

Here's a brief overview of the program's functionalities:

1. **Hand Gesture Recognition:** The program uses the MediaPipe library to detect and recognize hand gestures from the video feed captured by the computer's camera.

2. **Gesture Encoding:** The detected hand gestures are encoded using the `Gest` (Gesture) enumeration, which represents various hand poses such as fist, pinky, ring, mid, index, and more.

3. **Multi-Hand Recognition:** The program supports the recognition of gestures from both hands simultaneously. It classifies the major and minor hands based on their handedness and processes the gestures accordingly.

4. **Gesture-to-Action Mapping:** The recognized gestures trigger specific system actions. For example, the program can control the mouse cursor, simulate mouse clicks, adjust system volume and brightness, scroll vertically and horizontally, and perform other actions based on the interpreted gestures.

5. **Dampening for Cursor Stability:** The program includes a mechanism for stabilizing the cursor movement by applying dampening based on the distance traveled by the hand between consecutive frames.

6. **Control Initiation:** Certain gestures, such as pinch gestures, are initiated and controlled over a few frames, providing a smooth and controlled interaction
