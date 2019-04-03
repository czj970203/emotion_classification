import cv2
import time

# 图片识别方法封装
def discern(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cap = cv2.CascadeClassifier("/Users/chenzejun/desktop/haarcascade_frontalface_alt2.xml")
    faceRects = cap.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=3, minSize=(50, 50))
    if len(faceRects):
        for faceRect in faceRects:
            x, y, w, h = faceRect
            cv2.rectangle(img, (x, y), (x + h, y + w), (0, 255, 0), 2)  # 框出人脸
    return img
#    cv2.imshow("Processing", img)

'''
# 获取摄像头0表示第一个摄像头
cap = cv2.VideoCapture("/Users/chenzejun/desktop/HCI最终版.mp4")
startTime = time.time()
while (1):  # 逐帧显示
    ret, img = cap.read()
    nowTime = time.time()
    cv2.imshow("Image", img)
    diff = round(nowTime - startTime, 3) * 1000
    if(diff % 1000 <= 200):
        discern(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()  # 释放摄像头
cv2.destroyAllWindows()  # 释放窗口资源
'''