#######################################################
# RUN USING celery -A myshop worker -l info -P gevent #
#######################################################

##############################################################################
# USE STRIPE CLI  stripe listen --forward-to localhost:8000/payment/webhook/ #
##############################################################################

####################################################################################################
# USE RABITTMQ docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management #
####################################################################################################



from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
app = Celery('myshop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)