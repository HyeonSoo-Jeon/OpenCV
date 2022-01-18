import cv2

img = cv2.imread('./1.Img/img.jpg')
# img.shape : (390,640,3)
crop = img[100:200, 200:400]  # 세로 100~200, 가로 300~400

# 영역을 잘라서 기존 윈도우에 표시
img[100:200, 400:600] = crop


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
