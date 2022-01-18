# Canny Edge Detection
import cv2


def empty(pos):
    pass


img = cv2.imread('./15.Detection/snow.png')

name = 'TrackBar'
cv2.namedWindow(name)
cv2.createTrackbar('threshold1', name, 0, 255, empty)  # min
cv2.createTrackbar('threshold2', name, 0, 255, empty)  # max


while True:
    threshold1 = cv2.getTrackbarPos('threshold1', name)
    threshold2 = cv2.getTrackbarPos('threshold2', name)

    canny = cv2.Canny(img, threshold1, threshold2)

# 대상 이미지, 하위임계값, 상위임계값

    # cv2.imshow('img', img)
    cv2.imshow(name, canny)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
