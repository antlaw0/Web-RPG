import os
from flask import Flask
from flask import render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import Game


from models import User

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/executeCommand', methods=['POST'])
def command():
    command=request.form['command']
    output=Game.processCommandReturnJSON(command)
    return jsonify(output)


#if __name__ == '__main__':
#port = int(os.environ.get('PORT', 5000))
#app.run(host='127.0.0.1', port=port, debug=True)
