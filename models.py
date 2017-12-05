from app import db

#User accounts table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email
		
#Characters table
class Character(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	char1 = db.Column(db.String(10000))
	char2 = db.Column(db.String(10000))
    
	def __init__(self, id, char1, char2):
		self.id=id
		self.char1=char1
		self.char2=char2
	
	
	