from .extensions import socketio


@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)
    socketio.emit('message', data)
