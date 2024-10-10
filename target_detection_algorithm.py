import cv2
import numpy as np

# Load the image where the target is to be detected
image = cv2.imread('input_image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise and improve target detection
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply a threshold to create a binary image (black and white)
_, thresholded = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)

# Find contours in the binary image
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw the detected contours on the original image
output_image = image.copy()
cv2.drawContours(output_image, contours, -1, (0, 255, 0), 3)

# Count the number of detected targets
num_targets = len(contours)
print(f"Number of targets detected: {num_targets}")

# Show the images
cv2.imshow("Detected Targets", output_image)

# Wait for a key press and close the displayed windows
cv2.waitKey(0)
cv2.destroyAllWindows()