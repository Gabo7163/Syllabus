from PyQt5.QtCore import QObject, QThread
import pickle
import socket
import parametros as p


class ClienteHandlerThread(QThread):
    def __init__(self, client_socket, servidor):
        super().__init__()
        self.client_socket = client_socket
        self.servidor = servidor  # Referencia al servidor para acceder a sus métodos

    def run(self):
        try:
            while True:
                data_length = self.client_socket.recv(4)
                if not data_length:
                    break
                data_length = int.from_bytes(data_length, byteorder='big')
                data = self.client_socket.recv(data_length)
                command = pickle.loads(data)

                # Procesar los comandos recibidos del cliente
                if command["action"] == "verify_user":
                    self.servidor.verify_user(command["username"], self.client_socket)
                elif command["action"] == "record_score":
                    self.servidor.record_score(command["username"], command["score"])

        except (ConnectionResetError, EOFError):
            print("Conexión con el cliente cerrada.")
        finally:
            self.client_socket.close()



class Servidor(QObject):
    def __init__(self):
        super().__init__()
        print("Inicializando servidor...")
        self.host = p.HOST
        self.port = p.PORT
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind_and_listen()

    def bind_and_listen(self):
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen()
        print(f"Servidor escuchando en {self.host}:{self.port}...")
        self.accept_connections()

    def accept_connections(self):
        while True:
            client_socket, _ = self.socket_server.accept()
            client_thread = ClienteHandlerThread(client_socket, self)  # Crea el QThread personalizado
            client_thread.start()  # Inicia el hilo para manejar al cliente

    def verify_user(self, username, client_socket):
        # Verificación básica: el nombre debe tener al menos un carácter
        valid = len(username) > 0 and "," not in username
        response = {"valid": valid, "username": username}
        print(f"Verificación: {response}")
        self.send(response, client_socket)

    def record_score(self, username, score):
        with open("puntajes.txt", "a") as file:
            file.write(f"{username}: {score}\n")
        print(f"Puntaje registrado: {username} - {score}")

    def send(self, data, client_socket):
        msg_bytes = pickle.dumps(data)
        msg_length = len(msg_bytes).to_bytes(4, byteorder='big')
        client_socket.sendall(msg_length + msg_bytes)
        

if __name__ == "__main__":
    servidor = Servidor()