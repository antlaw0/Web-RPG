import os
from flask import Flask
from flask import render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import Game

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import User

@app.route('/', methods=['POST','GET'])
def index():
    #db.create_all()
    output=""
    if request.method == 'POST':
        command=request.form['command']
        output=Game.processCommand(command)
    return render_template('index.html', output=output)


#if __name__ == '__main__':
#port = int(os.environ.get('PORT', 5000))
#app.run(host='127.0.0.1', port=port, debug=True)
