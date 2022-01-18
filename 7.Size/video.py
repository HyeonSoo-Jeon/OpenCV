# 고정크기로 설정
import cv2

cap = cv2.VideoCapture('./2.Video/video.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    frame_resized = cv2.resize(frame, (400, 500))

# 비율로 설정
    frame_resized = cv2.resize(
        frame, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    cv2.imshow('video', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
