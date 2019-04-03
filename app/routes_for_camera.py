from flask import render_template, Response
from app.models import VideoCamera
from app import app
from backend import cv_capture
import cv2
import os

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

cap = VideoCamera()
is_closed = False

@app.route('/')
@app.route('/index')
def index():
    # jinja2模板，具体格式保存在index.html文件中
    return render_template('index.html', title="trial")


def gen(camera):
    while True:
        frame = camera.get_frame()
        # 使用generator函数输出视频流， 每次请求输出的content类型是image/jpeg
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')  # 这个地址返回视频流响应
def video_feed():
    return Response(gen(cap),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/close_video')
def close_video():
    cap.__del__()
    is_closed = True
    return render_template('index.html', is_closed=is_closed)

@app.route('/open_video')
def open_video():
    cap.__init__()
    is_closed = False
    return render_template('index.html', is_closed=is_closed)

@app.route('/analysis', methods=['GET', 'POST'])
def analysis():
    ret, img = cap.read()
    img = cv_capture.discern(img)
    basedir = os.path.abspath(os.path.dirname(__file__))
    write_path = os.path.join(basedir, 'static/cached_images.jpg')
    address = 'static/cached_images.jpg'
    cv2.imwrite(write_path, img)
    return render_template('index.html', address=address)

