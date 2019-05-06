import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from app.models import EmotionClassifier
import face_recognition

#用keras自带的后端来清理缓存，不能用tensorflow的！！！
import keras



emo = EmotionClassifier()
# 最大的玄学：热启动
hot = np.zeros((1, 48, 48, 1))
emo.emotion_classifier.predict(hot)


emotion_labels = {
    0: 'angry',
    1: 'disgust',
    2: 'fear',
    3: 'happy',
    4: 'sad',
    5: 'surprise',
    6: 'neutral'
}

#暂存柱状图数据，以免未识别出人脸时报错
cached_bar_data_multiple = []
cached_bar_data = []



def preprocess(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(basedir, 'haarcascade_frontalface_alt2.xml')
    cap = cv2.CascadeClassifier(file_path)
    faceRects = cap.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=3, minSize=(48, 48))
    length = len(faceRects)
    return gray, faceRects, length


# 图片识别方法封装
def discern(img, seen_face_encodings):
    gray, faceRects, length = preprocess(img)
    font = cv2.FONT_HERSHEY_SIMPLEX  # 字体
    for i in range(length):
        x, y, w, h = faceRects[i]
        face_location = []
        face_location.append((y, x + w, y + h, x))
        face_encoding = face_recognition.face_encodings(img, face_location)
        match_list = face_recognition.compare_faces(seen_face_encodings, face_encoding[0], tolerance=0.5)
        if True in match_list:
            # pos代表与哪张脸对应
            pos = 100
            for j in range(len(match_list)):
                if match_list[j]:
                    pos = j
                    break
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 框出人脸
            cv2.putText(img, 'No. '+str(pos + 1), (x + 20, y + 20), font, 2, (255, 0, 255), 4)
    return img


# 对视频帧进行处理
def get_processed_frame(image):
    #获取灰度图以及识别出的人脸
    gray, faceRects, length = preprocess(image)
    color = (0, 255, 0)  # 框色
    font = cv2.FONT_HERSHEY_SIMPLEX  # 字体
    if length > 4:
        length = 4
    for i in range(length):
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
    #    score = round(round(custom[0][emotion_label_arg] / np.sum(custom[0]), 2) * 100, 1)
        cv2.putText(image, '%s' % (i), (x + 30, y + 20), font, 1, (255, 0, 255), 4)
    ret, jpeg = cv2.imencode('.jpg', image)
    return jpeg.tobytes()


def classify(img, file_path):
    gray, faceRects, length = preprocess(img)
    if length > 4:
        length = 4
    for i in range(length):
        (x, y, w, h) = faceRects[i]
        gray_face = gray[(y):(y + h), (x):(x + w)]
        gray_face = cv2.resize(gray_face, (48, 48))
        gray_face = gray_face / 255.0
        gray_face = np.expand_dims(gray_face, 0)
        gray_face = np.expand_dims(gray_face, -1)
        global emo
        # 统一初始化的版本
        custom = emo.emotion_classifier.predict(gray_face)
        emotion_analysis(custom[0], i, file_path)
        keras.backend.clear_session()
    return length


def emotion_analysis(emotions, i, file_path):
    objects = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
    y_pos = np.arange(len(objects))
    plt.bar(y_pos, emotions, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('percentage')
    plt.title('emotions')
    root = os.getcwd()
    save_path = str(root) + file_path + str(i) + '.jpg'
    plt.savefig(save_path)
    plt.close()


#返回折线图数据
def process_line_chart(images, seen_face_encodings):
    line_results = {'1':[], '2':[], '3':[], '4':[]}
    count = 0
    for image in images:
        count += 1
        if count % 2 == 0:
            gray, faceRects, length = preprocess(image)
            if length != 0:
                for i in range(length):
                    (x, y, w, h) = faceRects[i]
                    face_location = []
                    face_location.append((y, x+w, y+h, x))
                    face_encoding = face_recognition.face_encodings(image, face_location)
                    match_list = face_recognition.compare_faces(seen_face_encodings, face_encoding[0], tolerance=0.6)
                    if True in match_list:
                        #pos代表与哪张脸对应
                        pos = 100
                        for j in range(len(match_list)):
                            if match_list[j]:
                                pos = j
                                break
                        gray_face = gray[(y):(y + h), (x):(x + w)]
                        gray_face = cv2.resize(gray_face, (48, 48))
                        gray_face = gray_face / 255.0
                        gray_face = np.expand_dims(gray_face, 0)
                        gray_face = np.expand_dims(gray_face, -1)
                        global emo
                        custom = emo.emotion_classifier.predict(gray_face)
                        prediction = custom[0].tolist()
                        for j in range(len(prediction)):
                            prediction[j] = round(prediction[j], 3)
                        line_results[str(pos + 1)].append(prediction)
    for k,v in line_results.items():
        leng = len(v)
        temp = np.array(v)
        temp = temp.reshape(7, leng)
        line_results[k] = temp.tolist()
    return line_results

#返回柱状图数据
def process_bar_chart(image):
    global cached_bar_data
    gray, faceRects, length = preprocess(image)
    if length != 0:
        (x, y, w, h) = faceRects[0]
        gray_face = gray[(y):(y + h), (x):(x + w)]
        gray_face = cv2.resize(gray_face, (48, 48))
        gray_face = gray_face / 255.0
        gray_face = np.expand_dims(gray_face, 0)
        gray_face = np.expand_dims(gray_face, -1)
        global emo
        custom = emo.emotion_classifier.predict(gray_face)
        cached_bar_data = custom[0].tolist()
    return cached_bar_data


#返回柱状图数据(多张人脸）
def process_bar_chart_multiple(image):
    global cached_bar_data_multiple
    gray, faceRects, length = preprocess(image)
    if length != 0:
        if length > 4:
            length = 4
        curr = []
        for i in range(length):
            (x, y, w, h) = faceRects[i]
            gray_face = gray[(y):(y + h), (x):(x + w)]
            gray_face = cv2.resize(gray_face, (48, 48))
            gray_face = gray_face / 255.0
            gray_face = np.expand_dims(gray_face, 0)
            gray_face = np.expand_dims(gray_face, -1)
            global emo
            custom = emo.emotion_classifier.predict(gray_face)
            curr.append(custom[0].tolist())
        cached_bar_data_multiple = curr
    return length, cached_bar_data_multiple


#获取面部关键信息
def get_key_face_info(img):
    face_locations = face_recognition.face_locations(img)
    face_encodings = face_recognition.face_encodings(img, face_locations)
    return face_locations, face_encodings

#返回折线图数据
def process_single_line_chart(image, seen_face_encodings):
    line_results = {'1':[], '2':[], '3':[], '4':[]}
    gray, faceRects, length = preprocess(image)
    if length != 0:
        for i in range(length):
            (x, y, w, h) = faceRects[i]
            face_location = []
            face_location.append((y, x+w, y+h, x))
            face_encoding = face_recognition.face_encodings(image, face_location)
            match_list = face_recognition.compare_faces(seen_face_encodings, face_encoding[0], tolerance=0.6)
            if True in match_list:
                #pos代表与哪张脸对应
                pos = 100
                for j in range(len(match_list)):
                    if match_list[j]:
                        pos = j
                        break
                gray_face = gray[(y):(y + h), (x):(x + w)]
                gray_face = cv2.resize(gray_face, (48, 48))
                gray_face = gray_face / 255.0
                gray_face = np.expand_dims(gray_face, 0)
                gray_face = np.expand_dims(gray_face, -1)
                global emo
                custom = emo.emotion_classifier.predict(gray_face)
                prediction = custom[0].tolist()
                line_results[str(pos + 1)]=prediction
    return line_results



