
"""
Simple celery script to test the workers machine
"""

from celery import Celery
from django.contrib.auth.models import User

app = Celery('tasks', backend='redis://redis.eastus.cloudapp.azure.com:6379',
             broker='amqp://altlegal:altlegal@vinta-devops-rabbitmq.eastus.cloudapp.azure.com/')


@app.task
def add():
    return User.objects.all()
