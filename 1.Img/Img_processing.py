import cv2

img = cv2.imread('./1.Img/img.jpg')
# imshow(창이름, 이미지 이름)
cv2.imshow('img', img)
# 지정된 시간(ms # 1000ms가 1초) 동안 사용자 키 입력 대기
key = cv2.waitKey(0)
# 모든 창 닫기
cv2.destroyAllWindows()

# 읽기 옵션
# cv2.IMREAD_COLOR # 컬러이미지, 투명영역은 무시(기본 값)
# cv2.IMREAD_GRAYSCALE # 흑백 이미지
# cv2.IMREAD_UNCHANGED # 투명 영역까지 포함
img = cv2.imread('./OpenCV/img.jpg', cv2.IMREAD_GRAYSCALE)

# Shape
# 이미지의 height, width, channel 정보
img.shape
# (390, 640, 3)
