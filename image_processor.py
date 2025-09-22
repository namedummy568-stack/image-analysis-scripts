
import cv2
import numpy as np

def load_image(image_path):
    """Loads an image from the specified path."""
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image from {image_path}")
    return image

def display_image(image, window_name='Image'):
    """Displays an image in a window."""
    if image is not None:
        cv2.imshow(window_name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def main():
    image_path = 'sample_image.jpg' # Placeholder
    image_data = load_image(image_path)
    if image_data is not None:
        print(f"Image loaded with shape: {image_data.shape}")
        display_image(image_data, 'Loaded Image')

if __name__ == "__main__":
    main()
