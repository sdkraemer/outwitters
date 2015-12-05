# all the imports
import os
import psycopg2
import urlparse
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy 

#app = Flask(__name__, static_url_path='')
app = Flask(__name__, static_url_path='')

# config
#from windows cmd prompt: set APP_SETTINGS=config.DevelopmentConfig
app.config.from_object(os.environ['APP_SETTINGS'])
print os.environ['APP_SETTINGS']
print os.environ['DATABASE_URL']


db = SQLAlchemy(app)

#conn = psycopg2.connect(
#	database=url.path[1:],
#    user=url.username,
#    password=url.password,
#    host=url.hostname,
#    port=url.port
#)



@app.route("/")
def hello():
	return render_template("index.html")
	

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
