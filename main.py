import cv2
import numpy as np

# Take input image from user
image_path = input("Enter the path to the image: ")

def cartoonize_image(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Check if image is loaded successfully
    if img is None:
        print("Error: Unable to load image. Please check the path.")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median blur to the grayscale image
    gray = cv2.medianBlur(gray, 5)

    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 10)

    # Apply bilateral filter to smooth the image while preserving edges
    color = cv2.bilateralFilter(img, 9, 250, 250)

    # Combine edges and color image to get cartoon effect
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Display result
    cv2.imshow('Cartoonized Image', cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the cartoonized image
    output_path = 'cartoonized_image.png'
    cv2.imwrite(output_path, cartoon)
    print(f"Cartoonized image saved as {output_path}")

# Call the function with user input
cartoonize_image(image_path)
