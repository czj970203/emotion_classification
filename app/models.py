import cv2
import os

#用tf的keras来加载模型是关键！！！
import tensorflow as tf


class VideoCamera(object):
    def __init__(self):
        # 通过opencv获取实时视频流
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # 因为opencv读取的图片并非jpeg格式，因此要用motion JPEG模式需要先将图片转码成jpg格式图片
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


    def read(self):
        ret, image = self.video.read()
        return ret, image


class EmotionClassifier(object):
    def __init__(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        model_path = os.path.join(basedir, 'backend/simple_CNN.530-0.65.hdf5')
        self.emotion_classifier = tf.keras.models.load_model(model_path)

