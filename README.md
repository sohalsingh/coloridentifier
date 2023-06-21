# coloridentifier


This Python script uses OpenCV to perform real-time color identification based on a camera feed. It captures frames from the camera, converts them to the HSV color space, and identifies the dominant color in each frame.

## Prerequisites

- Python 3.x
- OpenCV (cv2) library

## Installation

1. Clone the repository or download the script file.

2. Install the required libraries using pip:

   ```
   pip install opencv-python
   ```

## Usage

1. Connect a camera to your computer.

2. Run the script:

   ``````
   python coloridentifier.py
   ``````

3. A window will open showing the camera feed.

4. The script will identify the dominant color in each frame and display the color name on the window.

5. Press the 'q' key to exit the script.

## Customization

You can modify the script to add or modify color ranges for identification. Simply update the `color_ranges` dictionary in the `color_identifier` function. The script currently supports identification of "Red", "Green", and "Blue" colors, but you can add more color ranges as needed.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize the README file based on your specific requirements and preferences.
