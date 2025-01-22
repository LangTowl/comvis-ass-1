import os
import cv2
from utils import path, render_window



if __name__ == '__main__':
    print(f"Using cv2 version {cv2.__version__}\n")

    # Ensure path to image exists
    if os.path.exists(path):
        print(f"Path to '{path}' exists.\n")

        print("Press 's' to save image or 'q' to quit.\n")
        # Draw images in window
        render_window()
    else:
        print(f"Path to '{path}' does not exist.\n")