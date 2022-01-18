# 특정 크기를 초과하는 면적만

import cv2

img = cv2.imread('./15.Detection/card.png')
target_img = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(
    otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# 윤곽선 정보, 구조 = (대상 이미지, 윤곽선 찾는 모드, 윤곽선 찾을 때 근사치(method))
# CHAIN_APPROX_NONE : 모든 좌표
# CHAIN_APPROX_SIMPLE : 꼭지점 좌표, 사각형에 메모리를 줄일 수 있음

COLOR = (0, 200, 0)  # green

idx = 1
for cnt in contours:
    if cv2.contourArea(cnt) > 25000:
        x, y, width, height = cv2.boundingRect(cnt)
        cv2.rectangle(target_img, (x, y),
                      (x+width, y+height), COLOR, 2)  # 사각형 그림

        crop = img[y:y+height, x:x+width]
        cv2.imshow(f'card_crop_{idx}', crop)
        cv2.imwrite(f'card_crop_{idx}.png', crop)
        idx += 1

cv2.imshow('img', img)
cv2.imshow('otsu', otsu)
cv2.imshow('contour', target_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 윤곽선 찾기 모드
cv2.RETR_EXTERNAL  # 가장 외곽의 윤곽선만 찾음
cv2.RETR_LIST  # 모든 윤곽선을 찾음 (계층 정보 없음)
cv2.RETR_TREE  # 모든 윤곽선 찾음 (계층 정보를 트리구조)
