# Remove-Background

A simple Python script to remove the background from an image using OpenCV's GrabCut algorithm.

## Features

- Loads an image from a specified path
- Detects and masks the main subject
- Removes the background and displays the result

## Requirements

- Python 3.x
- [OpenCV](https://pypi.org/project/opencv-python/)
- [NumPy](https://pypi.org/project/numpy/)

## Usage

1. Install dependencies:
    ```bash
    pip install opencv-python numpy
    ```

2. Edit `Remove-Background.py` and set the path to your image:
    ```python
    img = cv2.imread('C:/path/to/your/image.png')  # Replace with your image path
    ```

3. Run the script:
    ```bash
    python Remove-Background.py
    ```

4. The script will display the original and background-removed images.

## Notes

- Adjust the rectangle in the script if the subject is not properly detected.
- The script works best with images where the subject is clearly separated from the background.
