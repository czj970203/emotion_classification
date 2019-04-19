import os
import time
import cv2
from flask import render_template, Response,request
from app import app
from app.backend import cv_capture
import keras
import numpy as np
import base64
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
cap = ''

#原始图片
image = ''
num = 0
is_uploaded = False

@app.route('/video')
def video():
    global cap
    basedir = os.path.abspath(os.path.dirname(__file__))
    video_path = os.path.join(basedir, 'static/videos/test1.flv')
    cap = cv2.VideoCapture(video_path)
    # jinja2模板，具体格式保存在index.html文件中
    return render_template('video.html', title="trial")


def gen():
    while True:
        global num
        num = num + 1
        success,frame = cap.read()
        # 使用generator函数输出视频流， 每次请求输出的content类型是image/jpeg
        if(num % 20 <= 10):
            jpeg = cv_capture.get_processed_frame(frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg + b'\r\n\r\n')
        else:
            ret, jpeg = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
        time.sleep(0.025)


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
    write_path = os.path.join(basedir, 'static/images/cached_video_images.jpg')
    address = 'static/images/cached_video_images.jpg'
    cv2.imwrite(write_path, img)
    global is_uploaded
    is_uploaded = True
    return render_template('video.html', address=address, is_uploaded=is_uploaded)


@app.route('/video_analysis')
def video_analysis():
    keras.backend.clear_session()
    length = cv_capture.classify(image, '/app/static/images/video_barchart')
    bar_addrs = []
    for i in range(length):
        temp = 'static/images/video_barchart' + str(i) + '.jpg'
        bar_addrs.append(temp)
    address = 'static/images/cached_video_images.jpg'
    global is_uploaded
    is_uploaded=False
    return render_template('video.html', address=address, bar_addrs=bar_addrs, is_uploaded=is_uploaded)


@app.route('/catch_image', methods=['GET', 'POST'])
def catch_image():
    url = request.form.get('imageData').split(',')[0]
    imageData = request.form.get('imageData').split(',')[1]
    img_b64decode = base64.urlsafe_b64decode(imageData) # base64解码
    img_array = np.fromstring(img_b64decode, np.uint8)  # 转换np序列
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR) # 转换Opencv格式
    global image
    #暂存原图
    image = img
    data = cv_capture.discern(img)
    basedir = os.path.abspath(os.path.dirname(__file__))
    write_path = os.path.join(basedir, 'static/images/cached_video_images.jpg')
    address = 'static/images/cached_video_images.jpg'
    cv2.imwrite(write_path, img)
    global is_uploaded
    is_uploaded = True
    ret,return_img = cv2.imencode('.jpg', img)  #转换成图片
    return_img = return_img.tobytes()
    imageData = base64.b64encode(return_img) #图片转换成base64
    return url + ',' + str(imageData,encoding='utf-8')

@app.route('/return_video_bar', methods=['POST', 'GET'])
def return_video_bar():
    imageData = request.form.get('imageData').split(',')[1]
    img_b64decode = base64.urlsafe_b64decode(imageData) # base64解码
    img_array = np.fromstring(img_b64decode, np.uint8)  # 转换np序列
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR) # 转换Opencv格式
    bar_data = cv_capture.process_bar_chart(img)
    bar_result = jsonify({'data': bar_data})
    return bar_result

