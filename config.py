import os

#default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = "key"
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	#windows cmd prompt: set DATABASE_URL='postgresql://localhost/outwitters_db'
	#SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/outwitters_db'
	
	
class DevelopmentConfig(BaseConfig):
	DEBUG = True
	
class ProductionConfig(BaseConfig):
	DEBUG = False	