import os
import cv2
from flask import render_template, Response
from app import app
from app.backend import cv_capture
from app.models import VideoCamera
import keras

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


cap = VideoCamera()
#原始图片
image = ''
is_stopped = False
is_closed = False
is_uploaded = False


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
        if is_closed == True:
            global is_stopped, is_closed_
            is_stopped = True
            break


@app.route('/video_feed')  # 这个地址返回视频流响应
def video_feed():
    return Response(gen(cap), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/close_video')
def close_video():
    global is_stopped, is_closed
    is_closed = True
    while not is_stopped:
        pass
    cap.__del__()
    return render_template('index.html', is_closed=is_closed)

@app.route('/open_video')
def open_video():
    cap.__init__()
    global is_stopped, is_closed
    is_stopped = False
    is_closed = False
    return render_template('index.html', is_closed=is_closed)

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


@app.route('/gen_bar')
def gen_bar():
    keras.backend.clear_session()
    cv_capture.classify(image)
    bar_addr = 'static/barchart.jpg'
    address = 'static/cached_images.jpg'
    global is_uploaded
    is_uploaded=False
    return render_template('index.html', address=address, bar_addr=bar_addr, is_uploaded=is_uploaded)


