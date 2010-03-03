DEBUG = False
TEMPLATE_DEBUG = DEBUG

DEFAULT_FROM_EMAIL = 'no-reply@dunkthemovie.com'

ADMINS = (
    ('Taylan Pince', 'taylanpince@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_NAME = 'dunk'
DATABASE_USER = 'dunkdbu'
DATABASE_PASSWORD = '1Mn35MSVS3'
DATABASE_HOST = '127.0.0.1'

MEDIA_URL = 'http://static.dunkthemovie.com/'
