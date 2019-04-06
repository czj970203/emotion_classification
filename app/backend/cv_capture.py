import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from app.models import EmotionClassifier


#用keras自带的后端来清理缓存，不能用tensorflow的！！！
import keras



emo = EmotionClassifier()
# 最大的玄学：热启动

hot = np.zeros((1, 48, 48, 1))
print(emo.emotion_classifier.predict(hot))

emotion_labels = {
    0: 'angry',
    1: 'disgust',
    2: 'fear',
    3: 'happy',
    4: 'sad',
    5: 'surprise',
    6: 'neutral'
}


def preprocess(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(basedir, 'haarcascade_frontalface_alt2.xml')
    cap = cv2.CascadeClassifier( r"C:\Program Files\Python37\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml")
    faceRects = cap.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=3, minSize=(48, 48))
    return gray, faceRects


# 图片识别方法封装
def discern(img):
    gray, faceRects = preprocess(img)
    if len(faceRects):
        for faceRect in faceRects:
            x, y, w, h = faceRect
            cv2.rectangle(img, (x, y), (x + h, y + w), (0, 255, 0), 2)  # 框出人脸
    return img


# 对视频帧进行处理
def get_processed_frame(camera):
    #利用camera读取一帧
    success, image = camera.read()
    #获取灰度图以及识别出的人脸
    gray, faceRects = preprocess(image)
    color = (0, 255, 0)  # 框色
    font = cv2.FONT_HERSHEY_SIMPLEX  # 字体
    for i in range(len(faceRects)):
        x, y, w, h = faceRects[i]
        gray_face = gray[(y):(y + h), (x):(x + w)]
        gray_face = cv2.resize(gray_face, (48, 48))
        gray_face = gray_face / 255.0
        gray_face = np.expand_dims(gray_face, 0)
        gray_face = np.expand_dims(gray_face, -1)
        #框出人脸
        cv2.rectangle(image, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)
        global emotion_labels, emo
        #对表情进行分类并给出评分
        custom = emo.emotion_classifier.predict(gray_face)
        emotion_label_arg = np.argmax(custom)
        emotion = emotion_labels[emotion_label_arg]
        score = round(custom[0][emotion_label_arg] / np.sum(custom[0]), 2) * 10
        cv2.putText(image, '%s: %f' % (emotion, score), (x + 30, y + 20), font, 1, (255, 0, 255), 4)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

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
        print(custom[0])
        #keras.backend.clear_session()
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
