import os
import time
import cv2
from flask import render_template, Response, jsonify
from app import app
from app.backend import cv_capture
from app.models import VideoCamera
import gc

#用keras自带的后端来清理缓存，不能用tensorflow的！！！
import keras


app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



#初始化摄像头
cap = VideoCamera()
#原始图片
image = ''
#是否停止传帧
is_stopped = False
#是否关闭摄像头
is_closed = False
#是否上传图片至网页
is_uploaded = False
#是否开始截取视频
start_collect = False
#是否结束截取视频
finish_collect = False
#统计已传帧的数量
frame_num = 0
#收集帧
collected_images = []


@app.route('/')
@app.route('/index')
def index():
    # jinja2模板，具体格式保存在index.html文件中
    return render_template('index.html', title="trial", is_closed=is_closed)


def gen(camera):
    global frame_num, collected_images
    while True:
        frame_num = (frame_num + 1) % 20
        ret, image = camera.read()
        if start_collect:
            collected_images.append(image)
        if frame_num < 10:
            frame = camera.get_frame()
        else:
            frame = cv_capture.get_processed_frame(image)

        # 使用generator函数输出视频流， 每次请求输出的content类型是image/jpeg
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        global is_stopped, is_closed
        if is_closed == True:
            is_stopped = True
            break


def gen_clips():
    global collected_images
    while True:
        temp = collected_images
        for image in temp:
            ret, jpeg = cv2.imencode('.jpg', image)
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
            time.sleep(0.075)



@app.route('/video_feed')  # 这个地址返回视频流响应
def video_feed():
    global cap
    return Response(gen(cap), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/close_video')
def close_video():
    global is_stopped, is_closed, cap
    is_closed = True
    while not is_stopped:
        pass
    cap.__del__()
    return render_template('index.html', is_closed=is_closed)


@app.route('/open_video')
def open_video():
    global cap
    cap = VideoCamera()
    global is_stopped, is_closed
    is_stopped = False
    is_closed = False
    return render_template('index.html', is_closed=is_closed)


@app.route('/analysis', methods=['GET', 'POST'])
def analysis():
    global image, cap
    ret, img = cap.read()
    #暂存原图
    image = img
    img = cv_capture.discern(img)
    basedir = os.path.abspath(os.path.dirname(__file__))
    write_path = os.path.join(basedir, 'static/images/cached_images.jpg')
    address = 'static/images/cached_images.jpg'
    cv2.imwrite(write_path, img)
    global is_uploaded
    is_uploaded = True
    return render_template('index.html', address=address, is_uploaded=is_uploaded)


@app.route('/gen_bar')
def gen_bar():
    keras.backend.clear_session()
    length = cv_capture.classify(image, '/app/static/images/barchart')
    bar_addrs = []
    for i in range(length):
        temp = 'static/images/barchart' + str(i) + '.jpg'
        bar_addrs.append(temp)
    address = 'static/images/cached_images.jpg'
    global is_uploaded
    is_uploaded=False
    return render_template('index.html', address=address, bar_addrs=bar_addrs, is_uploaded=is_uploaded)


@app.route('/collect_frames')
def collect_frames():
    global start_collect, finish_collect, collected_images
    collected_images.clear()
    start_collect = True
    finish_collect = False
    return render_template('index.html', start_collect=start_collect, finish_collect=finish_collect)


@app.route('/stop_collect')
def stop_collect():
    global start_collect, finish_collect
    start_collect = False
    finish_collect = True
    return render_template('index.html', start_collect=start_collect, finish_collect=finish_collect)


@app.route('/feed_video_clips')
def feed_video_clips():
    global finish_collect
    if finish_collect:
        return Response(gen_clips(), mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return 'No frames are collected!'


@app.route('/return_bar', methods=['POST', 'GET'])
def return_bar():
    global cap
    gc.collect()
    if not is_closed:
        ret, img = cap.read()
        length, bar_data = cv_capture.process_bar_chart_multiple(img)
        bar_result = jsonify({'data': bar_data})
    else:
        bar_result = jsonify({'data': 'camera closed.'})
    return bar_result


@app.route('/return_line', methods=['POST', 'GET'])
def return_line():
    global collected_images
    line_data = cv_capture.process_line_chart(collected_images)
    line_result = jsonify({'data': line_data})
    return line_result








