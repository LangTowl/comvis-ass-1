import os
import cv2
from utils import path, update_contrast, update_brightness, render_window


if __name__ == '__main__':
    print(f"Using cv2 version {cv2.__version__}\n")

    # Ensure path to image exists
    if os.path.exists(path):
        print(f"Path to '{path}' exists.\n")

        # Generate window for rendering
        cv2.namedWindow('Assignment 1 - Lang Towl', cv2.WINDOW_AUTOSIZE)

        # Render sliders
        cv2.createTrackbar('Brightness', 'Assignment 1 - Lang Towl', 128, 255, update_brightness)
        cv2.createTrackbar('Contrast', 'Assignment 1 - Lang Towl', 128, 255, update_contrast)

        # Draw images in indow
        render_window()

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print(f"Path to '{path}' does not exist.\n")