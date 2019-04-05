import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from app.models import EmotionClassifier
import keras


emo = EmotionClassifier()
# 最大的玄学：热启动
hot = np.zeros((1, 48, 48, 1))
print(emo.emotion_classifier.predict(hot))



def preprocess(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(basedir, 'haarcascade_frontalface_alt2.xml')
    cap = cv2.CascadeClassifier(file_path)
    faceRects = cap.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=3, minSize=(50, 50))
    return gray, faceRects


# 图片识别方法封装
def discern(img):
    gray, faceRects = preprocess(img)
    if len(faceRects):
        for faceRect in faceRects:
            x, y, w, h = faceRect
            cv2.rectangle(img, (x, y), (x + h, y + w), (0, 255, 0), 2)  # 框出人脸
    return img


def classify(img):
    gray, faceRects = preprocess(img)
    color = (255, 0, 0)
    for(x, y, w, h) in faceRects:
        gray_face = gray[(y):(y + h), (x):(x + w)]
        gray_face = cv2.resize(gray_face, (48, 48))
        gray_face = gray_face / 255.0
        gray_face = np.expand_dims(gray_face, 0)
        gray_face = np.expand_dims(gray_face, -1)
        global emo
        # 统一初始化的版本
        custom = emo.emotion_classifier.predict(gray_face)
        emotion_analysis(custom[0])
        keras.backend.clear_session()


def emotion_analysis(emotions):
    objects = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
    y_pos = np.arange(len(objects))
    plt.bar(y_pos, emotions, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('percentage')
    plt.title('emotions')
    root = os.getcwd()
    save_path = os.path.join(root, 'app/static/barchart.jpg')
    plt.savefig(save_path)
    plt.close()
