from flask_socketio import SocketIO, send
from flask import Flask , render_template
import motorConversacional as mc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
	return render_template('index.html')

#Decorador que escucha por un evento, en este caso un evento 'message'
@socketio.on('connect')
def handle_connect():
	print('Usuario conectado')

@socketio.on('message')
def handle_message(msg):
	print('Mensaje recibido:' + msg)
	system_response = mc.genera_respuesta(msg)
	send(system_response, broadcast=True)   #broadcast=True envía el mensaje a todos los usuarios conectados
	
    
if __name__ == "__main__":
	#app.run()
	socketio.run(app, debug=True)