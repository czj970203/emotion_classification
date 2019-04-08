import os

import cv2
from flask import render_template, Response
from app import app
from app.backend import cv_capture
import keras

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

cap=cv2.VideoCapture('E:\\1.mp4')
#原始图片
image = ''
num = 0;
is_uploaded = False
@app.route('/video')
def video():
    # jinja2模板，具体格式保存在index.html文件中
    return render_template('video.html', title="trial")


def gen():
    while True:
        global num
        num = num + 1
        success,frame = cap.read()
        # 使用generator函数输出视频流， 每次请求输出的content类型是image/jpeg
        if(num % 20 == 5 ):
            frame=cv_capture.discern(frame)
            jpeg = cv_capture.get_processed_frame(frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg + b'\r\n\r\n')
        else:
            ret, jpeg = cv2.imencode('.jpg', frame)
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

@app.route('/catch', methods=['GET', 'POST'])
def catch():
    ret, img = cap.read()
    global image
    #暂存原图
    image = img
    img = cv_capture.discern(img)
    basedir = os.path.abspath(os.path.dirname(__file__))
    write_path = os.path.join(basedir, 'static/cached_video_images.jpg')
    address = 'static/cached_video_images.jpg'
    cv2.imwrite(write_path, img)
    global is_uploaded
    is_uploaded = True
    return render_template('video.html', address=address, is_uploaded=is_uploaded)

@app.route('/video_analysis')
def video_analysis():
    keras.backend.clear_session()
    cv_capture.classify(image)
    #keras.backend.clear_session()
    bar_addr = 'static/video_barchart.jpg'
    address = 'static/cached_video_images.jpg'
    global is_uploaded
    is_uploaded=False
    return render_template('video.html', address=address, bar_addr=bar_addr, is_uploaded=is_uploaded)