# 텍스트
# OpenCV에서 사용하는 글꼴 종류

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
cv2.FONT_HERSHEY_SIMPLEX  # 보통 크기의 산 세리프(sans-serif) 글꼴
cv2.FONT_HERSHEY_PLAIN  # 작은 크기의 산 세리프 글꼴
cv2.FONT_HERSHEY_SCRIPT_SIMPLEX  # 필기체 스타일 글꼴
cv2.FONT_HERSHEY_TRIPLEX  # 보통 크기의 산 세리프 글꼴
cv2.FONT_ITALIC  # 기울임(이탤릭체)


img = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR = (255, 255, 255)  # white
THICKNESS = 1
SCALE = 1

cv2.putText(img, "It's a test Text!", (25, 50),
            cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, "It's a test Text!", (25, 150),
            cv2.FONT_HERSHEY_PLAIN, SCALE, COLOR, THICKNESS)
cv2.putText(img, "It's a test Text!", (25, 250),
            cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, "It's a test Text!", (25, 350),
            cv2.FONT_HERSHEY_TRIPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, "It's a test Text!", (25, 450),
            cv2.FONT_HERSHEY_TRIPLEX | cv2.FONT_ITALIC, SCALE, COLOR, THICKNESS)
# 그릴 위치, Text, 시작 위치, 폰트, 크기, 색깔


# 한글우회
# PIL (Python Image Library)


def myPutText(src, text, pos, font_size, font_color):
    img_pil = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype('fonts/gulim.ttc', font_size)
    draw.text(pos, text, font=font, fill=font_color)
    return np.array(img_pil)


FONT_SIZE = 30
COLOR = (255, 255, 255)  # 흰색

img = myPutText(img, "한글 우회", (40, 50), FONT_SIZE, COLOR)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
