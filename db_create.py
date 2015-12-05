from app import db
from models import GameState

#create the database and the tables
db.create_all()

#insert
db.session.add(GameState("Test1"))
db.session.add(GameState("Test2"))

#commit changes
db.session.commit()