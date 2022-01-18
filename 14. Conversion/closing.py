# 팽창 후 침식. 구멍을 메운 다음 다시 깎음

import cv2
import numpy as np

kernel = np.ones((3, 3), dtype=np.uint8)
img = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)

dilate = cv2.dilate(img, kernel, iterations=3)
erode = cv2.erode(dilate, kernel, iterations=3)


cv2.imshow('img', erode)
cv2.waitKey(0)
cv2.destroyAllWindows()
