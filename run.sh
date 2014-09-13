#!/bin/sh

pkill restorus_pid
../bin/gunicorn --config restorus/gunicorn.py restorus.wsgi:application --daemon --pid restorus_pid