import cv2

img = cv2.imread('./1.Img/img.jpg')

# 시계방향
rotate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
rotate_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)


cv2.imshow('img', img)
cv2.imshow('img', rotate_90)
cv2.imshow('img', rotate_180)
cv2.imshow('img', rotate_270)
cv2.waitKey(0)
cv2.destroyAllWindows(0)
