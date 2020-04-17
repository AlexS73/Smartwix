command = '/root/code/env/bin/start_gunicorn'
pythonpath = '/root/code/SmartWix'
bind = '127.0.0.1:8001'
workers = 3
user = 'root'
limit_request_fields = 32000
limit_requset_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=SmartWix.settings'
