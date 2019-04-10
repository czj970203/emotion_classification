from flask import Flask
from flask_apscheduler import APScheduler


scheduler = APScheduler()


app = Flask(__name__)
#app.config.from_object(Config)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


from app import routes_for_video
from app import routes_for_camera
from app import models

