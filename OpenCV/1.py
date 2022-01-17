import cv2

img = cv2.imread('./OpenCV/img.jpg')
# imshow(창이름, 이미지 이름)
cv2.imshow('img', img)
# 지정된 시간 동안 사용자 키 입력 대기
cv2.waitKey(0)
# 모든 창 닫기
cv2.destroyAllWindows()
