import cv2

# 흑백으로 읽음
img = cv2.imread('./1.Img/img.jpg', cv2.IMREAD_GRAYSCALE)
# 흑백으로 변경
dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


cv2.imshow('img', img)
cv2.imshow('gray', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
