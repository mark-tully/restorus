# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l)k#x&#3d%r746samad9*$=wo&#8(l0=#wha2x^oe$v%_44+)d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'restorusdb',
        'USER': 'restorusdb',
        'PASSWORD': 'gildah4mf4st-',
        'HOST': 'localhost'
    }
}