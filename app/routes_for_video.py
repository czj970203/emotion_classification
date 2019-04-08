import os

import cv2
from flask import render_template, Response
from app import app
from app.backend import cv_capture
import keras

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

basedir = os.path.abspath(__file__)
video_path = os.path.join(basedir, 'static/HCI最终版.mp4')
cap=cv2.VideoCapture(video_path)
#原始图片
num = 0
@app.route('/video')
def video():
    # jinja2模板，具体格式保存在index.html文件中
    return render_template('video.html', title="trial")


def gen():
    while True:
        global num
        num = num + 1
        success,frame = cap.read()
        jpeg = frame
        if(num % 20 <= 5 ):
            jpeg = cv_capture.discern(frame)
        ret, jpeg = cv2.imencode('.jpg', jpeg)
        # 使用generator函数输出视频流， 每次请求输出的content类型是image/jpeg
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')


@app.route('/video_play')  # 这个地址返回视频流响应
def video_play():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/play_video/<video_address>',methods=['POST','GET'])
def play_video(video_address):
    global cap
    cap = cv2.VideoCapture(video_address)
    return render_template('video.html')
