from flask import render_template, Response
import cv2
from app import app


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