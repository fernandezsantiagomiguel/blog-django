from .base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost'] #aqui deberia agregarse el dominio de la pagina noticias.com ej

# Hay que cambiar el engine por django.db.backends.postgresql o .mysql  
# dependiendo de que lenguaje se use a la hora de deployar
DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    #NAME :os.gatenv('DB_NAME'),
    #USER:-----------('DB_USER'),
    #PASSWORD:-----------('DB_PASSWORD'),
    #HOST:-----------(DB_HOST),
    #PORT:-----------('DB_PORT'),
    }
}
os.environ['DJANGO_PORT'] = '8080'