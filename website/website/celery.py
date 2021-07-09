from __future__ import absolute_import

import os
import django
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()


app = Celery('website')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'update-stnk-status-task': {
        'task': 'stnk.tasks.update_stnk_status',
        'schedule': 1 * 60,
        'args': ()
    },
}
# schedule 1 * 60 = 1 menit
# schedule 1 * 60 * 60  = 1 jam