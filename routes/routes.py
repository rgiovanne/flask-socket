from resources.socket import ReactSocket, testeEmit



class View():
    def rotas(api,socketio):
        
        socketio.on_event('react', ReactSocket.handle_react)
        # socketio.on_event('connect', ReactSocket.test_connect)
        
        # Register

        api.add_resource(testeEmit, '/testeEmit')
       