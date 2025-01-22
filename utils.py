import cv2
import numpy as np



# Path to image source
path = 'dog.bmp'

# Load image from path
image = cv2.imread(path)
new_image = image.copy()

def render_histogram(reference):
    # Split the image into its color channels
    channels = cv2.split(reference)
    colors = ['blue', 'green', 'red']
    channel_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

    # Create a blank canvas to draw the histogram (might need to change dimensions later?)
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

def update_brightness(val):
    global new_image

    # Adjust brightness based on slider value
    alpha = val / 128
    new_image = cv2.convertScaleAbs(image, alpha = alpha)

    # Generate histograms
    image_hist = render_histogram(image)
    bright_hist = render_histogram(new_image)

    # Resize histograms to match image dimensions
    height, width, _ = image.shape
    resized_image_hist = cv2.resize(image_hist, (width, height))
    resized_bright_hist = cv2.resize(bright_hist, (width, height))

    # Generate canvas for rendering
    image_stack = np.hstack([image, new_image])
    hist_stack = np.hstack([resized_image_hist, resized_bright_hist])
    canvas = np.vstack([image_stack, hist_stack])

    # Display the image with adjusted brightness
    cv2.imshow('Assignment 1 - Lang Towl', canvas)

def update_contrast(val):
    global new_image

    # Adjust contrast based on slider value
    beta = val - 128
    new_image = cv2.convertScaleAbs(image, beta = beta)

    # Generate histograms
    image_hist = render_histogram(image)
    contrast_hist = render_histogram(new_image)

    # Resize histograms to match image dimensions
    height, width, _ = image.shape
    resized_image_hist = cv2.resize(image_hist, (width, height))
    resized_contrast_hist = cv2.resize(contrast_hist, (width, height))

    # Generate canvas for rendering
    image_stack = np.hstack([image, new_image])
    hist_stack = np.hstack([resized_image_hist, resized_contrast_hist])
    canvas = np.vstack([image_stack, hist_stack])

    # Display the image with adjusted contrast
    cv2.imshow('Assignment 1 - Lang Towl', canvas)

def render_window():
    # Generate windows for rendering
    cv2.namedWindow('Assignment 1 - Lang Towl', cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow('Controller', cv2.WINDOW_AUTOSIZE)
    cv2.resizeWindow('Controller', 1000, 1000)

    # Render sliders
    cv2.createTrackbar('Brightness', 'Controller', 128, 255, update_brightness)
    cv2.createTrackbar('Contrast', 'Controller', 128, 255, update_contrast)

    # Call update functions
    update_brightness(128)
    update_contrast(128)

    while True:
        # Listen for key press
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            print('Attempting to Save...\n')

            try:
                cv2.imwrite(path, new_image)
                print("Image saved!\n")
            except Exception as e:
                print(f'Error Saving Image: {e}\n')
        elif key == ord('q'):
            print('Exiting...\n')
            break

    # Terminate windows
    cv2.destroyAllWindows()