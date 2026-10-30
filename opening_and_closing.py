# Opening and Closing Operations Using OpenCV
# Developed By: Subashini K
# Register No: 212225240160

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Original Image
img = cv2.imread("tulips.jpg")
if img is None:
    img = cv2.imread("flower.jpg")

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")
plt.show()

# 2. Opening Operation
kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
plt.imshow(cv2.cvtColor(opening, cv2.COLOR_BGR2RGB))
plt.title("Opening")
plt.axis("off")
plt.show()

# 3. Closing Operation
kernel = np.ones((5, 5), np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
plt.imshow(cv2.cvtColor(closing, cv2.COLOR_BGR2RGB))
plt.title("Closing")
plt.axis("off")
plt.show()
