import os

#default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = "key"
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	
	
class DevelopmentConfig(BaseConfig):
	DEBUG = True
	
class ProductionConfig(BaseConfig):
	DEBUG = False	