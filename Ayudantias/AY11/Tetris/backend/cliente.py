import socket
import pickle
from PyQt5.QtCore import QObject, pyqtSignal, QThread
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import os
import parametros as p


class Cliente(QObject):
    # Señales para comunicar con el frontend
    senal_usuario_verificado = pyqtSignal(bool)
    senal_mensaje_error = pyqtSignal()
    senal_empezar_juego = pyqtSignal(str)

    def __init__(self, ruta_cancion):
        super().__init__()
        self.host = p.HOST
        self.port = p.PORT
        self.ruta_cancion = ruta_cancion

        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectado = False
        self.conectar_al_servidor()

    def iniciar_musica(self):
        self.musica = Musica(self.ruta_cancion)
        self.musica.comenzar()

    def conectar_al_servidor(self):
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.conectado = True
            print("Cliente conectado exitosamente al servidor.")
            # Iniciar hilo para escuchar respuestas del servidor
            self.thread_escucha = QThread()
            self.thread_escucha.run = self.escuchar_respuestas
            self.thread_escucha.start()
        except ConnectionError:
            print("Error al intentar conectarse al servidor.")
            self.socket_cliente.close()

    def escuchar_respuestas(self):
        while self.conectado:
            try:
                data_length = self.socket_cliente.recv(4)
                if not data_length:
                    break
                data_length = int.from_bytes(data_length, byteorder='big')
                data = self.socket_cliente.recv(data_length)
                respuesta = pickle.loads(data)

                # Procesar la respuesta del servidor
                if "valid" in respuesta and respuesta["valid"]:
                    self.senal_empezar_juego.emit(respuesta["username"])

                elif "valid" in respuesta and not respuesta["valid"]:
                    self.senal_mensaje_error.emit()

            except (ConnectionResetError, EOFError):
                print("Conexión con el servidor cerrada.")
                break

    def enviar_comando(self, comando):
        if self.conectado:
            try:
                msg_bytes = pickle.dumps(comando)
                msg_length = len(msg_bytes).to_bytes(4, byteorder='big')
                self.socket_cliente.sendall(msg_length + msg_bytes)
            except BrokenPipeError:
                print("Error al enviar comando. \
                       Conexión con el servidor cerrada.")

    def verificar_usuario(self, username):
        comando = {"action": "verify_user", "username": username}
        self.enviar_comando(comando)

    def enviar_puntaje(self, username, score):
        comando = {
            "action": "record_score",
            "username": username,
            "score": score
        }
        self.enviar_comando(comando)


class Musica(QObject):
    
    def __init__(self, ruta_cancion):
        super().__init__()
        self.ruta_cancion = ruta_cancion

    def comenzar(self):
        try:
            self.player = QMediaPlayer(self)
            path = os.path.abspath(self.ruta_cancion)
            if not os.path.isfile(path):
                raise FileNotFoundError(f"El archivo '{path}' no fue encontrado.")
                
            cancion = QMediaContent(QUrl.fromLocalFile(path))
            self.player.setMedia(cancion)
            self.player.play()
            self.player.mediaStatusChanged.connect(self.loopear_cancion)
        
        except FileNotFoundError as error:
            print('Error: archivo de música no encontrado:', error)
        
        except ValueError as error:
            print('Error de valor al cargar el archivo de música:', error)
        
        except RuntimeError as error:
            print('Error en el sistema multimedia:', error)

    def loopear_cancion(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.player.setPosition(0)
            self.player.play()
