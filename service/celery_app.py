import os
import time

from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'absconfig.settings')


app = Celery('absconfig.settings')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()


@app.task()
def debug_task():
    time.sleep(20)
    print("Hello from debug_task")