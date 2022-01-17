# 2. 동영상 출력

import cv2
cap = cv2.VideoCapture('./2.Video/video.mp4')

while cap.isOpened():  # 동영상 파일이 열려있는지?
    ret, frame = cap.read()
    # ret : 성공 여부
    # frame : 받아온 이미지
    if not ret:
        print('no more frames to receive')
        break

    cv2.imshow('video', frame)

    if cv2.waitKey(1) == ord('q'):
        print('terminated by user input')
        break

cap.release()  # 자원 해제
cv2.destroyAllWindows()
