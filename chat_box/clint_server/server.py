
from flask import *
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'i am the hacker u cant hack me'
socketio = SocketIO(app, cors_allowed_origins='*')


@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	
	send(msg, broadcast=True)

if __name__ == '__main__':
	socketio.run(app)