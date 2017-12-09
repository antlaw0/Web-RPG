from app import db

#User accounts table
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80))
	email = db.Column(db.String(120), unique=True)
	password = db.Column(db.String(80))
    
	def __init__(self, email, username,password):
		self.username = username
		self.email = email
		self.password=password
		
#Characters table
class Character(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	character1 = db.Column(db.String(10000))
	character2 = db.Column(db.String(10000))
    
	def __init__(self, id, char1String, char2String):
		self.id=id
		self.character1=char1String
		self.character2=char2String
	
	
	