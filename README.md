# OPENING--AND-CLOSING
## Aim
To implement Opening and Closing using Python and OpenCV.

## Software Required
1. Anaconda - Python 3.7
2. OpenCV
## Algorithm:
### Step 1: Import Libraries
Import the necessary libraries: OpenCV for image processing and NumPy for array manipulation.

### Step 2: Create or Load an Image
Create a binary image or load an existing image where you want to apply the morphological operations. Ensure that the image is in grayscale format.

### Step 3: Define the Structuring Element
Define a structuring element (kernel) using cv2.getStructuringElement(). Common shapes include rectangular, elliptical, or cross-shaped kernels.

### Step 4: Apply Morphological Operations
Opening: Apply the opening operation using cv2.morphologyEx() with the cv2.MORPH_OPEN flag. This operation removes small objects (noise) from the foreground of the image.
Closing: Apply the closing operation using cv2.morphologyEx() with the cv2.MORPH_CLOSE flag. This operation closes small holes in the foreground objects.
### Step 5: Display Results
Use matplotlib to display the original image, the opened image, and the closed image side by side for comparison.
 
## Program:

``` Python
import cv2
import numpy as np
from matplotlib import pyplot as plt

image1 = np.zeros((200, 200), dtype='uint8')
cv2.rectangle(image1, (50, 50), (150, 150), 255, -1)
cv2.rectangle(image1, (60, 60), (140, 140), 255, -1)
cv2.rectangle(image1, (20, 20), (40, 40), 255, -1)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
image_open = cv2.morphologyEx(image1, cv2.MORPH_OPEN, kernel)
image_close = cv2.morphologyEx(image1, cv2.MORPH_CLOSE, kernel)

plt.subplot(1, 3, 1), plt.imshow(image1, 'gray'), plt.title('Original Image')
plt.subplot(1, 3, 2), plt.imshow(image_open, 'gray'), plt.title('Opened Image')
plt.subplot(1, 3, 3), plt.imshow(image_close, 'gray'), plt.title('Closed Image')
plt.show()

```
## Output:
![image](https://github.com/user-attachments/assets/bf92bd55-1bbf-4742-a0e6-802e8d501832)

## Result
Thus the Opening and Closing operation is used in the image using python and OpenCV.
