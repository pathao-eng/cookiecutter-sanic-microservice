from celery import Celery
from .config import CELERY_BROKER_URL

app = Celery('{{cookiecutter.app_name}}', broker=CELERY_BROKER_URL)


@app.task
def hello():
    return 'Hello from {{cookiecutter.app_name}}!'
