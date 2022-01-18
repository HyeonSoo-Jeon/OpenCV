# face Detection : 얼굴임만 인식
# face Recognition : 누구의 얼굴인지 인식

import cv2
import mediapipe as mp


def overlay(image, x, y, w, h, overlay_image):  # 대상이미지,x,y,width,height, 덮어씌울 이미지
    alpha = overlay_image[:, :, 3]  # BGRA
    mask_image = alpha / 255  # 0~1 사이의 값을 가지게 됨(1은 불투명, 0은 투명)

    for c in range(0, 3):  # channel : BGR
        image[y-h:y+h, x-w:x+w, c] = (overlay_image[:, :, c]
                                      * mask_image)+image[y-h:y+h, x-w:x+w, c] * (1-mask_image)


# 얼굴을 찾고 찾은 얼굴에 표시를 해주는 변수 정의
mp_face_detection = mp.solutions.face_detection  # 얼굴 검출 face_detection 모듈 사용
mp_drawing = mp.solutions.drawing_utils  # 얼굴 특징을 그리기 위한 drawing_utils 모듈 사용

cap = cv2.VideoCapture('./17.Face/face_video.mp4')

img_right_eye = cv2.imread('./17.Face/right_eye.png',
                           cv2.IMREAD_UNCHANGED)  # 100 * 100
img_left_eye = cv2.imread('./17.Face/left_eye.png', cv2.IMREAD_UNCHANGED)
img_nose = cv2.imread('./17.Face/nose.png', cv2.IMREAD_UNCHANGED)

# model_selection의 값 : 0(2m 근거리), 1(5m 원거리)
# min_detection_confidence : 얼굴 정확도
with mp_face_detection.FaceDetection(
        model_selection=0, min_detection_confidence=0.7) as face_detection:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break

        # 성능 향상
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # 얼굴 검출
        results = face_detection.process(image)

        # Draw the face detection annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # 검출된 얼굴 이 있으면은
        if results.detections:
            # 오른눈, 왼쪽눈, 코, 입, 오른귀, 왼쪽귀
            for detection in results.detections:
                # 얼굴에 그려줌
                # mp_drawing.draw_detection(image, detection)

                # 특정 위치 가져오기
                keypoints = detection.location_data.relative_keypoints
                right_eye = keypoints[0]
                left_eye = keypoints[1]
                nose_tip = keypoints[2]

                # 이미지로 부터 크기 정보
                h, w, _ = image.shape

                # 이미지 실제 좌표 (X,Y)
                right_eye = (int(right_eye.x * w), int(right_eye.y * h))
                left_eye = (int(left_eye.x * w), int(left_eye.y * h))
                nose_tip = (int(nose_tip.x * w), int(nose_tip.y * h))

                # cv2.circle(image, right_eye, 50, (255, 0, 0), 10, cv2.LINE_AA)
                # cv2.circle(image, left_eye, 50, (0, 255, 0), 10, cv2.LINE_AA)
                # cv2.circle(image, nose_tip, 50, (0, 0, 255), 10, cv2.LINE_AA)

                # 이미지 그리기
                # image[right_eye[1] - 50:right_eye[1] + 50,
                #       right_eye[0]-50:right_eye[0]+50] = img_right_eye
                # image[left_eye[1] - 50:left_eye[1] + 50,
                #       left_eye[0]-50:left_eye[0]+50] = img_left_eye
                # image[nose_tip[1] - 50:nose_tip[1] + 50,
                #       nose_tip[0]-50:nose_tip[0]+50] = img_nose

                overlay(image, *right_eye, 50, 50, img_right_eye)
                overlay(image, *left_eye, 50, 50, img_left_eye)
                overlay(image, nose_tip[0], nose_tip[1]-30, 50, 50, img_nose)
        cv2.imshow('MediaPipe Face Detection',
                   cv2.resize(image, None, fx=0.5, fy=0.5))
        if cv2.waitKey(1) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
