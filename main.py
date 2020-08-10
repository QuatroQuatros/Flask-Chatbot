import time
from flask import Flask
from flask_socketio import SocketIO, emit, send
from bot import Bot

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def hello():
	return open('templates/index.html').read()


@socketio.on('message')
def message_recv(data):
	bot = Bot('Eva')
	emit('message',data,broadcast=True)
	a = bot.mensagem(data)
	emit('message',a,broadcast=True)


if __name__ == '__main__':
	socketio.run(app,'127.0.0.1',3000)