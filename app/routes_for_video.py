import os

import cv2
from flask import render_template, Response
from app import app
from app.backend import cv_capture
from app.models2 import VideoCamera
import keras

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

cap=VideoCamera()
#原始图片
image = ''

@app.route('/video')
def video():
    # jinja2模板，具体格式保存在index.html文件中
    return render_template('video.html', title="trial")


def gen(video):
    while True:
        frame = video.get_frame()
        # 使用generator函数输出视频流， 每次请求输出的content类型是image/jpeg
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_play')  # 这个地址返回视频流响应
def video_play():
    return Response(gen(video), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/play_video/<video_address>',methods=['GET'])
def play_video(video_address):
    global cap
    cap = cv2.VideoCapture(video_address)
    return render_template('video.html')
