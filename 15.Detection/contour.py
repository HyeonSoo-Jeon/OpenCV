# 경계선을 연결한 선
import cv2

img = cv2.imread('./15.Detection/card.png')
target_img = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(
    otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# 윤곽선 정보, 구조 = (대상 이미지, 윤곽선 찾는 모드, 윤곽선 찾을 때 근사치(method))

COLOR = (0, 200, 0)  # green
THICKNESS = 2
cv2.drawContours(target_img, contours, -1, COLOR, THICKNESS)  # 윤곽선 그리기

cv2.imshow('img', img)
cv2.imshow('otsu', otsu)
cv2.imshow('contour', target_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 윤곽선 찾기 모드
cv2.RETR_EXTERNAL  # 가장 외곽의 윤곽선만 찾음
cv2.RETR_LIST  # 모든 윤곽선을 찾음 (계층 정보 없음)
cv2.RETR_TREE  # 모든 윤곽선 찾음 (계층 정보를 트리구조)
