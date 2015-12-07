# all the imports
import os
import psycopg2
import urlparse
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy 
from functools import wraps

app = Flask(__name__, static_url_path='')
app.secret_key = "my key"

#login required decorator
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('login'))
	return wrap


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
@login_required
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
	map = Map.query.filter_by(name="Candy Core Mine", is_preloaded=True).first()
	return map.state
	
@app.route("/map/preloaded/sugarrock")
def getSugarRock():
	map = Map.query.filter_by(name="Sugar Rock", is_preloaded=True).first()
	return map.state
	
@app.route("/map/preloaded/acrospire")
def getAcrospire():
	map = Map.query.filter_by(name="Acrospire", is_preloaded=True).first()
	return map.state
	
@app.route("/map/preloaded/blitzbeach")
def getBlitzBeach():
	map = Map.query.filter_by(name="Blitz Beach", is_preloaded=True).first()
	return map.state
	
@app.route("/map/preloaded/mechanism")
def getMechanism():
	map = Map.query.filter_by(name="Mechanism", is_preloaded=True).first()
	return map.state
	
@app.route("/map/preloaded/machination")
def getMachination():
	map = Map.query.filter_by(name="Machination", is_preloaded=True).first()
	return map.state
	
@app.route('/login', methods=['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid credentials. admin/admin are the credentials.'
		else:
			session['logged_in'] = True
			flash('You were just logged in!')
			return redirect(url_for('index'))
	return render_template('login.html', error=error)
	
@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in',None)
	flash('You were just logged out!')
	return redirect(url_for('welcome'))
	

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
