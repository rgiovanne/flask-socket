
from flask_restful import Resource
from flask_socketio import emit,send
from flask_socketio import ConnectionRefusedError

class ReactSocket():
    def handle_react(json):
        print('RECEBENDO JSON:' + str(json))
        # emit('flask',json)
    

class testeEmit(Resource):
    def get(self):
        emit('flask',"NOVA NOTA", namespace='/chat')
    
    # def test_connect(auth):
    #     if not self.authenticate(request.args):
    #         raise ConnectionRefusedError('unauthorized!')
    #     emit('my response', {'data': 'Connected'})
    
        