# 도형 그리기

# 빈 스케치북 만들기

from turtle import color
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

# 원
COLOR = (255, 2550)  # BGR : 민트
RADIUS = 50  # 반지름
THICKNESS = 10  # 두께

cv2.circle(img, (200, 100), RADIUS, COLOR, THICKNESS, cv2.LINE_AA)  # 속이 빈 원
cv2.circle(img, (400, 100), RADIUS, COLOR, cv2.FILLED, cv2.LINE_AA)  # 속이 찬 원
# 그릴 위치, 원의 중심, 반지름, 색깔, 두께, 선 종류

# 사각형
COLOR = (0, 255, 0)  # BGR : Green
THICKNESS = 3

cv2.rectangle(img, (100, 100), (200, 200), COLOR, THICKNESS)  # 속이 빈 사각형
cv2.rectangle(img, (200, 200), (300, 300), COLOR, cv2.FILLED)
# 그림 위치, 왼쪽 위 좌표, 오른쪽 아래 좌표, 색깔, 두께


# 다각형
COLOR = (0, 0, 255)  # BGR : Green
THICKNESS = 3

pts1 = np.array([[100, 200], [200, 300], [100, 300]])
pts2 = np.array([[300, 200], [400, 200], [400, 300]])
# cv2.polylines(img, [pts1], True, COLOR, THICKNESS, cv2.LINE_AA)
# cv2.polylines(img, [pts2], True, COLOR, THICKNESS, cv2.LINE_AA)
cv2.polylines(img, [pts1, pts2], True, COLOR, THICKNESS, cv2.LINE_AA)
# 그릴 위치, 그릴 좌표들, 닫힘 여부(첫, 끝점 연결), 색깔, 두께, 선 종류
pts3 = np.array([[[200, 300], [300, 400], [200, 400]],
                 [[400, 400], [500, 300], [500, 400]]])
cv2.fillPoly(img, pts3, COLOR, cv2.LINE_AA)
# 그릴 위치, 그릴 좌표들, 색깔, 선 종류

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
