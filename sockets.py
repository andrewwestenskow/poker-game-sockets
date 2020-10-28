from flask import Flask
from flask_socketio import SocketIO, join_room, leave_room, emit
from utils.socketprint import print_green
app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('join')
def handle_join(data):
  print_green('SOCKET JOINED')
  print_green(data)
  join_room(data['room'])
  emit('game state', 'This is the game state', room = data['room'])

if __name__ == '__main__':
  socketio.run(app)