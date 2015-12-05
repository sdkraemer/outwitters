from app import db

class GameState(db.Model):
	__tablename__='game_state'
	
	game_state_id = db.Column(db.Integer, primary_key=True)
	map_state = db.Column(db.LargeBinary)
	
	def __init__(self, map_state):
		self.map_state = map_state
	
	def __repr__(self):
		return '<{}>'.format(self.map_state)