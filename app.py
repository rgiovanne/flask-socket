from config.blacklist import BLACKLIST
from flask import jsonify, session
from flask_jwt_extended import JWTManager
from flask_restful import Api,request
from routes.routes import View
from flask_socketio import SocketIO
from config.appConfig import create_app

app = create_app()
socketio = SocketIO(app,cors_allowed_origins="*")
api = Api(app)
jwt = JWTManager(app)


@jwt.token_in_blocklist_loader
def verifica_blacklist(self, token):
    return token['jti'] in BLACKLIST


@jwt.revoked_token_loader
def token_de_acesso_invalido(jwt_header, jwt_payload):
    return jsonify({"message": "You have been logged out."}, 401)

clients = []

@socketio.on('connect', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    # Add client to client list
    clients.append(request.sid)

    room = session.get('room')
    # join_room(room)

    # emit to the first client that joined the room
    

# Rotas
View.rotas(api,socketio)

@app.route('/teste', methods=['GET'])
def version():
    socketio.emit('flask', {'msg': 'Vitor has entered the room.'}, room=clients[1], namespace='/chat')
    return {"Version": "1.0.0"}


if __name__ == '__main__':
    socketio.run(app, '0.0.0.0')