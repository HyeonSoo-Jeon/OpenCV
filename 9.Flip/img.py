import cv2
from numpy import flip

img = cv2.imread('./1.Img/img.jpg')

flip_horizontal = cv2.flip(img, 1)  # 1 좌우, 0 상하
flip_vertical = cv2.flip(img, 0)  # 1 좌우, 0 상하
flip_both = cv2.flip(img, -1)  # 상하좌두 다 대칭


cv2.imshow('img', flip_horizontal)
cv2.imshow('img', flip_vertical)
cv2.imshow('img', flip_both)
cv2.waitKey(0)
cv2.destroyAllWindows()
