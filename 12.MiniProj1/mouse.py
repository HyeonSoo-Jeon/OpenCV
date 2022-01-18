# 마우스 이벤트 등록
import cv2


def mouse_handler(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('LBtn DOWN')
    elif event == cv2.EVENT_LBUTTONUP:
        print('LBtn UP')
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print('LBtn DBL')
    elif event == cv2.EVENT_RBUTTONDOWN:
        print('RBtn DOWN')


img = cv2.imread('./11.Transformation/poker.jpg')

cv2.namedWindow("img")  # img란 윈도우를 미리 만듬
cv2.setMouseCallback('img', mouse_handler)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
