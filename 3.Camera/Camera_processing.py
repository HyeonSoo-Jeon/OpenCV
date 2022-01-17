# 카메라 출력

import cv2

cap = cv2.VideoCapture(0)  # 0번째 카메라 장치 [Device ID]

if not cap.isOpened():
    print('camera not opened')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    flip_frame = cv2.flip(frame, 1)
    # 반전, 1은 좌우 0은 상하
    cv2.imshow('camera', flip_frame)

    if cv2.waitKey(1) == ord('q'):
        print('terminated by user input')
        break

cap.release()
cv2.destroyAllWindows()
