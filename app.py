import os
from flask import Flask
from flask import render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import jsonify

app = Flask(__name__)
app.secret_key = os.urandom(12)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
migrate = Migrate(app, db)
import Game
import models

#db.drop_all()
#db.create_all()

def userExists(email):
	found=False
	if models.User.query.filter_by(email=email).first() != None:
		found = True
	return found

def insertUser(email, username, password):
	u=models.User(email,username,password)
	db.session.add(u)
	db.session.commit()
		
def getId(email):
	u=models.User.query.filter_by(email=email).first()
	return u.id
	
def getPassword(email):
	u=models.User.query.filter_by(email=email).first()
	return u.password
	
def getUsername(email):
	u=models.User.query.filter_by(email=email).first()
	return u.username
	
@app.route('/', methods=['POST','GET'])
def index():
    if 'email' in session:
        
        return render_template('game.html', output="Welcome back.", username=session['username'])
    else:
        message=None
        if request.method=='POST':
            
            email = request.form['email']
            password = request.form['password']
            #if entered email exists
            if userExists(email) == True:
                #if password matches password in database
                if getPassword(email) == password:
                    session['username']=getUsername(email)
                    session['id']=getId(email)
                    session['email'] = email
                    return render_template('game.html', output="Hi there.", username=session['username'])
    
                else:
                    message="Invalid password"
                    return render_template('index.html', message=message)

            else:
                message="User with that e-mail does not exist"
                return render_template('index.html', message=message)

        else:
           return render_template('index.html', message=message)
	
	
@app.route('/registration', methods=['GET', 'POST'])
def registration():

    messages = []
    
    if request.method=='POST':
        email=request.form['email']
        username = request.form['username']
        password = request.form['password']
        password2=request.form['password2']
        #check if password and re-entered passwords match
        if password != password2:
            messages.append("Invalid password- passwords do not match. Please re-enter password")
            
        #check username length
        if len(username) < 1:
            messages.append("Invalid username")
        if len(username) > 20:
            messages.append("Invalid username- The entered username is too long. Usernames must be 20 characters or less in length.")
        
        #check password length
        if len(password) < 8:
            messages.append("Invalid password- passwords must be at least 8 characters long.")
        if len(password) > 20:
            messages.append("Invalid password- The password you entered is too long. Passwords must not be longer than 20 characters in length.")
        
        #if no error messages
        if len(messages) != 0:
            #return registration page with new error message(s)
            return render_template('registration.html', messages=messages)
        
        if userExists(email) == True:
            messages.append("User with that e-mail already exists")
            return render_template('registration.html', messages=messages)
        else:
            #insert new user
            insertUser(email, username, password)
            session['username'] = username
            session['id']=getId(email)
            session['email']=email
            return render_template('game.html', output="Welcome back.", username=session['username'])
    
    else:
        return render_template('registration.html', messages=messages)
    
	
@app.route('/game', methods=['POST'])
def runGame():
	if 'email' in session:
		output="Welcome to The Game."
		return render_template('game.html', output=output)
	else:
		message="Please log in."
		return render_template('index.html',message=message)
	
@app.route('/executeCommand', methods=['GET', 'POST'])
def command():
    command=request.form['command']
    output=Game.main(session['id'], command)
    #return jsonify(output)
    return render_template('game.html', output=output)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port, debug=True)