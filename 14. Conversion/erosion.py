# 이미지를 깎아서 노이즈 제거
# 흰색 영역을 없애서 검정으로 바꿈


import cv2
import numpy as np

kernel = np.ones((3, 3), dtype=np.uint8)
img = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)

erode1 = cv2.erode(img, kernel, iterations=1)  # 반복횟수
erode2 = cv2.erode(img, kernel, iterations=2)  # 반복횟수
erode3 = cv2.erode(img, kernel, iterations=3)  # 반복횟수


cv2.imshow('gray', erode3)
cv2.waitKey(0)
cv2.destroyAllWindows()
