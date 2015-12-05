# all the imports
import os
import psycopg2
import urlparse
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy 

#app = Flask(__name__, static_url_path='')
from app import app

# config
#from windows cmd prompt: set APP_SETTINGS=config.DevelopmentConfig
app.config.from_object(os.environ['APP_SETTINGS'])
print os.environ['APP_SETTINGS']


#app.config['DATABASE_URL'] = 'postgres://ytwqouuptiuoln:t83695HzdbyVS7SYHONXpfGDYJ@ec2-54-204-40-209.compute-1.amazonaws.com:5432/d93uu3ukjciuo6'
#app.config['DATABASE_URL'] = 'postgresql://localhost/outwitters_db'
#SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

#urlparse.uses_netloc.append("postgres")
#url = urlparse.urlparse(os.environ["DATABASE_URL"])

#conn = psycopg2.connect(
#	database=url.path[1:],
#    user=url.username,
#    password=url.password,
#    host=url.hostname,
#    port=url.port
#)

# Create our database model
class GameState(db.Model):
    __tablename__ = "game_state"
    id = db.Column(db.Integer, primary_key=True)
    map_state = db.Column(db.String)

    def __init__(self, map_state):
        self.map_state = map_state

    def __repr__(self):
        return '<id %r>' % self.id

@app.route("/")
def hello():
	return render_template("index.html")
	

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
