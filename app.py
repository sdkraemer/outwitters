# all the imports
import os
import psycopg2
import urlparse
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy 

app = Flask(__name__, static_url_path='')

# config
#from windows cmd prompt: set APP_SETTINGS=config.DevelopmentConfig
app.config.from_object(os.environ['APP_SETTINGS'])
print os.environ['APP_SETTINGS']
print os.environ['DATABASE_URL']


db = SQLAlchemy(app)

class GameState(db.Model):
	__tablename__= 'game_state'
	
	game_state_id = db.Column(db.Integer, primary_key=True)
	map_state = db.Column(db.LargeBinary)
	
	def __init__(self, map_state):
		self.map_state = map_state
	
	def __repr__(self):
		return '<{}>'.format(self.map_state)
		
print GameState.query.all()


@app.route("/")
def index():
	return render_template("index.html")
	
@app.route("/game/<int:id>")
def getGame(id):
	game = GameState.query.filter_by(game_state_id=id).first()
	return game.map_state
	

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
