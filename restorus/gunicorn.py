import sys
import os
import multiprocessing

bind = '127.0.0.1:8003'
worker_class = 'gevent'
workers = multiprocessing.cpu_count() * 2 + 1
django_settings = 'restorus.settings'