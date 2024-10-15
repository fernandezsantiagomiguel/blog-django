from .base import *

DEBUG = False

# TODO: Dejar solo el dominio de produccion
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# TODO: Cambiar la config de la base de datos para la produccion
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3'

        # En caso de usar postgresql
        # 'ENGINE': 'django.db.backends.postgresql'

        # En caso de usar mysql
        # 'ENGINE': 'django.db.backends.mysql'

        # ''NAME': os.getenv('DB_NAME') 

        # 'USER': os.getenv('DB_USER')

        # 'PASSWORD': os.getenv('DB_PASSWORD')

        # 'HOST': os.getenv('DB_HOST')

        # 'PORT': os.getenv('DB_PORT')
    }
}

os.environ['DJANGO_PORT'] = '8080'