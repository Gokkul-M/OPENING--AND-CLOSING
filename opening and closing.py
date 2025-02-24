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
