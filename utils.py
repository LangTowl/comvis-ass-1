import cv2
import numpy as np

# Path to source image
path = 'dog.bmp'

# Load image from path
image = cv2.imread(path)
new_image = image.copy()


def render_histogram(reference):
    # Split the image into its color channels
    channels = cv2.split(reference)
    colors = ['blue', 'green', 'red']  # Corresponds to BGR channels
    channel_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # B, G, R

    # Create a blank canvas to draw the histogram
    hist_canvas = np.zeros((300, 512, 3), dtype=np.uint8)

    for channel, color in zip(channels, channel_colors):
        # Calculate the histogram for each channel
        hist = cv2.calcHist([channel], [0], None, [256], [0, 256])

        # Normalize the histogram to fit in the canvas height
        cv2.normalize(hist, hist, 0, hist_canvas.shape[0], cv2.NORM_MINMAX)

        # Draw the histogram on the canvas
        for x in range(1, len(hist)):
            cv2.line(
                hist_canvas,
                (int((x - 1) * (512 / len(hist))), 300 - int(hist[x - 1])),
                (int(x * (512 / len(hist))), 300 - int(hist[x])),
                color, 2
            )

    return hist_canvas


# Create a function to change brightness
def update_brightness(val):
    # Adjust brightness based on slider value
    alpha = val / 128
    bright_image = cv2.convertScaleAbs(new_image, alpha=alpha)

    # Generate histograms
    image_hist = render_histogram(image)
    bright_hist = render_histogram(bright_image)

    # Resize histograms to match image dimensions
    height, width, _ = image.shape
    resized_image_hist = cv2.resize(image_hist, (width, height))
    resized_bright_hist = cv2.resize(bright_hist, (width, height))

    # Generate canvas for rendering
    image_stack = np.hstack([image, bright_image])
    hist_stack = np.hstack([resized_image_hist, resized_bright_hist])
    canvas = np.vstack([image_stack, hist_stack])

    # Display the image with adjusted brightness
    cv2.imshow('Assignment 1 - Lang Towl', canvas)

def update_contrast(val):
    # Adjust contrast based on slider value
    beta = val - 128
    contrast_image = cv2.convertScaleAbs(new_image, beta=beta)

    # Generate histograms
    image_hist = render_histogram(image)
    contrast_hist = render_histogram(contrast_image)

    # Resize histograms to match image dimensions
    height, width, _ = image.shape
    resized_image_hist = cv2.resize(image_hist, (width, height))
    resized_contrast_hist = cv2.resize(contrast_hist, (width, height))

    # Generate canvas for rendering
    image_stack = np.hstack([image, contrast_image])
    hist_stack = np.hstack([resized_image_hist, resized_contrast_hist])
    canvas = np.vstack([image_stack, hist_stack])

    # Display the image with adjusted contrast
    cv2.imshow('Assignment 1 - Lang Towl', canvas)

def render_window():
    update_brightness(128)
    update_contrast(128)