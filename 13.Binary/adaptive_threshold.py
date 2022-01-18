# 이미지를 작은 영역으로 나누어서 임계치 적용

import cv2
from numpy import block


def empty(pos):
    pass


img = cv2.imread('./13.Binary/book.jpg', cv2.IMREAD_GRAYSCALE)


# Trackbar : 값 변화에 따른 변형 확인
name = 'Trackbar'
cv2.namedWindow(name)

cv2.createTrackbar('block_size', name, 25, 100, empty)  # 홀수만 가능, 1보다 큼
cv2.createTrackbar('c', name, 3, 10, empty)  # 일반적으로 양수의 값을 사용
# bar 이름, 창 이름, 초기값, 최대값, 이벤트 처리

while True:
    block_size = cv2.getTrackbarPos('block_size', name)
    c = cv2.getTrackbarPos('c', name)

    if block_size <= 1:
        block_size = 3

    if block_size % 2 == 0:
        block_size += 1
    # bar 이름, 창 이름
    binary = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, c)

    cv2.imshow(name, binary)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
