import os

import cv2
from flask import render_template, Response
from app import app
from app.backend import cv_capture
from app.models import VideoCamera

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

cap = cv2.VideoCapture("/Users/chenzejun/desktop/HCI最终版.mp4")
is_stopped = False

@app.route('/')

@app.route('/video')
def index():
    # jinja2模板，具体格式保存在video.html文件中
    return render_template('video.html', title="trial")
def gen(camera):
    while True:
        frame = camera.get_frame()
        # 使用generator函数输出视频流， 每次请求输出的content类型是image/jpeg
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        if is_stopped == True:
            break

@app.route('/video/<video_address>',methods=['GET', 'POST'])  # 这个地址返回视频流响应
def video_feed(video_address=None):
    return render_template('video.html', video_address=video_address)

@app.route('/analysis', methods=['GET', 'POST'])
def analysis():
    ret, img = cap.read()
    global image
    image = img
    img = cv_capture.discern(img)
    basedir = os.path.abspath(os.path.dirname(__file__))
    write_path = os.path.join(basedir, 'static/cached_images.jpg')
    address = 'static/cached_images.jpg'
    cv2.imwrite(write_path, img)
    global is_uploaded
    is_uploaded = True
    return render_template('index.html', address=address, is_uploaded=is_uploaded)