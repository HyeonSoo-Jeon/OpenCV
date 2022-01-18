# 고정 크기로 설정
import cv2

img = cv2.imread('./1.Img/img.jpg')
dst = cv2.resize(img, (400, 500))  # width, height 고정 크기

# 비율로 설정
dst = cv2.resize(img, None, fx=0.5, fy=0.5)  # x,y 비율 정의


# 보간법
cv2.INTER_AREA: 크기 줄일 때 사용
cv2.INTER_CUBIC: 크기 늘릴 때 사용(속도 느림, 퀄리티 좋음)
cv2.INTER_LINEAR: 크기 늘릴 때 사용(기본 값)

dst = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
dst = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)


cv2.imshow('img', img)
cv2.imshow('resize', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
