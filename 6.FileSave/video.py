import cv2

cap = cv2.VideoCapture('./2.Video/vide.mp4')

# 코덱 정의
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 프레임 크기, FPS
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
# fps = cap.get(cv2.CAP_PROP_FPS) * 2 # 영상 재생 속도 2배

out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))
# 저장 파일명, 코덱, fps, 크기(width, height)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    out.write(frame)  # 영상 데이터만 저장(소리 X)
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()
