import cv2
import numpy as np

img = cv2.imread('./11.Transformation/poker.jpg')

width, height = 530, 710

src = np.array([[702, 143], [1133, 414], [726, 1007], [
               276, 700]], dtype=np.float32)  # input 개 지정
dst = np.array([[0, 0], [width, 0], [width, height],
                [0, height]], dtype=np.float32)
# 좌상, 우상, 우하, 좌하 (시계 방향)

matrix = cv2.getPerspectiveTransform(src, dst)
result = cv2.warpPerspective(img, matrix, (width, height))  # matrix 대로 변환을 함


cv2.imshow('img', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
