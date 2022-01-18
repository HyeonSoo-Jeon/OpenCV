# 이미지 파일 저장

import cv2
img = cv2.imread('./1.Img/img.jpg', cv2.IMREAD_GRAYSCALE)  # 흑백으로 이미지 불러오기
result = cv2.imwrite('img_save.png', img)
if result:
    print('save successfully')
