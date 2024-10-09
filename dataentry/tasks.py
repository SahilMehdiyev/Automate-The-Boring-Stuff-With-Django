from awd_main.celery import app
import time

@app.task
def celery_test_task():
    time.sleep(3)
    return 'Task executed successfully'