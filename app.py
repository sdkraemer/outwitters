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

class Map(db.Model):
	__tablename__= 'map'
	
	id = db.Column(db.Integer, primary_key=True)
	state = db.Column(db.LargeBinary)
	name = db.Column(db.Text)
	author = db.Column(db.Text)
	is_preloaded = db.Column(db.Boolean)
	
	def __init__(self, state, name, author, is_preloaded):
		self.state = state
		self.name = name
		self.author = author
		self.is_preloaded = is_preloaded
	
	def __repr__(self):
		return '<state - {}>'.format(self.state)
		


@app.route("/")
def index():
	return render_template("index.html")
	
@app.route("/map/<int:id>", methods=['GET'])
def getMap(id):
	map = Map.query.filter_by(id=id).first()
	return map.state
	
@app.route("/map", methods=['POST'])
def saveGame():
	print request.form
	return "test return"
	
@app.route("/map/preloaded/candycoremine")
def getCandyCoreMine():
	return "json here:"
	
@app.route("/map/preloaded/sugarrock")
def getSugarRock():
	return "json here:"
	
@app.route("/map/preloaded/acrospire")
def getAcrospire():
	return "json here:"
	
@app.route("/map/preloaded/blitzbeach")
def getBlitzBeach():
	return "json here:"
	
@app.route("/map/preloaded/mechanism")
def getMechanism():
	return "json here:"
	
@app.route("/map/preloaded/machination")
def getMachination():
	return "json here:"
	

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
