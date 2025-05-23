import cv2
import numpy as np

# ****** Opening and Displaying the Original Image ******

img = cv2.imread('C:/path/to/your/image.png')  # Replace with your image path
if img is None:
    raise FileNotFoundError("Image not found. Check the file path.")

grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Input_Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ****** Detecting and Masking the subject ******

test_mask = np.zeros(img.shape[:2], np.uint8)

# Specify the foreground and background
rect = (50, 50, img.shape[1] - 100, img.shape[0] - 100)  # Adjust rectangle to fit the image
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# GrabCut algorithm to refine mask
cv2.grabCut(img, test_mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# Refine mask
test_mask = np.where((test_mask == cv2.GC_PR_BGD) | (test_mask == cv2.GC_BGD), 0, 1).astype('uint8')

# ****** Applying the Mask ******

img = img * test_mask[:, :, np.newaxis]

# Display the processed image
cv2.imshow('Input_Image_Without_Background', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
