# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7z4%tgfe7fds83-gji_+1mv)m_0x%1_oxz@+n^u0w)4+ul#1%@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'restorusdb',
        'USER': 'restorusdb',
        'PASSWORD': 'n30h0bb1t-',
        'HOST': 'localhost'
    }
}