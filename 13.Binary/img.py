from tkinter.tix import Tree
import cv2


def empty(pos):
    print(pos)


img = cv2.imread('./13.Binary/book.jpg', cv2.IMREAD_GRAYSCALE)

# ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# cv2.imshow('img', img)
# cv2.imshow('bin', binary)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Trackbar : 값 변화에 따른 변형 확인
name = 'Trackbar'
cv2.namedWindow(name)

cv2.createTrackbar('threshold', name, 127, 255, empty)
# bar 이름, 창 이름, 초기값, 최대값, 이벤트 처리

while True:
    thresh = cv2.getTrackbarPos('threshold', name)
    # bar 이름, 창 이름
    ret, binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)

    if not ret:
        break
    cv2.imshow(name, binary)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
