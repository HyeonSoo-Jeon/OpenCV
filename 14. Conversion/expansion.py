# 흰색 영역의 외곽 픽셀 주변에 흰색을 추가

import cv2
import numpy as np

kernel = np.ones((3, 3), dtype=np.uint8)
img = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)

dilate1 = cv2.dilate(img, kernel, iterations=1)  # 반복횟수
dilate2 = cv2.dilate(img, kernel, iterations=2)  # 반복횟수
dilate3 = cv2.dilate(img, kernel, iterations=3)  # 반복횟수

cv2.imshow('gray', dilate3)
cv2.waitKey(0)
cv2.destroyAllWindows()
