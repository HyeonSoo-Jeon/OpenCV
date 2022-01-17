# 도형 그리기

# 빈 스케치북 만들기

import cv2
import numpy as np

# 세로 480 x 가로 640, 3 Channel[RGB]
# np.zeros : 0으로 공간을 채우기
img = np.zeros((480, 640, 3), dtype=np.uint8)

# BGR를 모두 흰 색으로 채우기, RGB순서가 아님
img[:] = (255, 255, 255)

# 일부 영역 색칠
# 세로기준 100~200, 가로기준 200~300
img[100:200, 200:300] = (0, 0, 0)


# 직선
# 직선의 종류 (list type)

# cv2.LINE_4 : 상하좌우 4방향, 선이 이어져야함
# cv2.LINE_8 : 대각선을 포함한 8방향 (기본값), 선이 끊어질 수 있음
# cv2.LINE_AA : 부드러운 선(anti-aliasing)

COLOR = (0, 255, 255)  # BGR : Yellow
THICKNESS = 3  # 두께

cv2.line(img, (50, 100), (400, 50), COLOR, THICKNESS, cv2.LINE_8)  # (x,y)
cv2.line(img, (50, 200), (400, 150), COLOR, THICKNESS, cv2.LINE_4)  # (x,y)
cv2.line(img, (50, 300), (400, 250), COLOR, THICKNESS, cv2.LINE_AA)  # (x,y)
# 그릴 위치, 시작 점, 끝 점, 색깔 두께, 선 종류


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
