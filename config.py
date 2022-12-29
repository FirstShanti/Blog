import os
import locale

from datetime import timedelta, datetime

from dotenv import dotenv_values
from utils import randomString

env = dotenv_values(".env")
basedir = os.path.abspath(os.path.dirname(__file__))
locale.setlocale(locale.LC_ALL, "")
local = locale.getdefaultlocale()[0]
lang = {'ru_RU':{'comment':['вчера в ', 'сегодня в ', 'в']},
        'en_US':{'comment':['yesterday at ', 'today at ', 'at']},
		'ua_UA':{'comment':['вчора в ', 'сьогодні в ', 'в']}
    }

login_stamp = datetime.today().strftime('%Y:%m:%d - %H')

class Configuration(object):
	DEBUG = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	CKEDITOR_PKG_TYPE = "standard"

	SECRET_KEY = 'sfsdfsdf' #randomString()
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

	JWT_SECRET_KEY = 'sfsdfsdf' #randomString()
	JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
	JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)
	JWT_TOKEN_LOCATION = ['cookies']
	JWT_EXPIRATION_DELTA = timedelta(hours=1)
	JWT_VERIFY_CLAIMS = ['exp']
	JWT_COOKIE_CSRF_PROTECT = False

	SEND_FILE_MAX_AGE_DEFAULT = 0

	WTF_CSRF_CHECK_DEFAULT = False

	FLASK_ADMIN_SWATCH = 'cerulean'

class Development(Configuration):
	DEBUG = True
	PORT = 5001

	HOST = "0.0.0.0"

	SQLALCHEMY_DATABASE_URI = env.get('DATABASE_URL')
	MAIL_USERNAME = env.get('MAIL_USERNAME')
	MAIL_PASSWORD = env.get('MAIL_PASSWORD')


class Production(Configuration):

	HOST = os.environ.get('HOST')
	PORT = os.environ.get('PORT')
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

	def __init__(self) -> None:
		super().__init__()
		self.fix_heroku_dialect()

	def fix_heroku_dialect(self):
		if self.SQLALCHEMY_DATABASE_URI.split(':/')[0] == 'postgres':
			self.SQLALCHEMY_DATABASE_URI = self.SQLALCHEMY_DATABASE_URI.replace('postgres', 'postgresql')


environments = {
	'Development': Development,
	'Production': Production
}