from random import choice
import socket
import threading
import requests


class Tareo:
    def __init__(self, port: int, host: str) -> None:
        print("Inicializando servidor...")
        self.host = host
        self.port = port
        self.respuestas = ["No puedes usar esa libreria",
                            "No es un problema de los tests",
                            "Actualizamos los tests",
                            "Puedes usar esa librería :D"]
        
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind_and_listen()
        self.accept_connections()


    def bind_and_listen(self) -> None:
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen()
        print(f"Servidor escuchando en {self.host}:{self.port}...")


    def accept_connections(self) -> None:
        thread = threading.Thread(target=self.accept_connections_thread)
        thread.start()


    def accept_connections_thread(self) -> None:
        print("Servidor aceptando conexiones...")

        while True:
            client_socket, _ = self.socket_server.accept()
            listening_client_thread = threading.Thread(
                target=self.listen_client_thread,
                args=(client_socket, ))
            listening_client_thread.start()


    def send(self, value: any, sock: socket.socket) -> None:
        stringified_value = str(value)
        msg_bytes = stringified_value.encode()
        msg_length = len(msg_bytes).to_bytes(4, byteorder='big')
        sock.sendall(msg_length + msg_bytes)


    def listen_client_thread(self, client_socket: socket.socket) -> None:
        print("Servidor conectado a un nuevo cliente...")

        while True:
            response_bytes_length = client_socket.recv(4)
            response_length = int.from_bytes(
                response_bytes_length, byteorder='big')
            
            response_length = int.from_bytes(response_bytes_length, byteorder='big')
            pregunta = client_socket.recv(response_length).decode()

            print(f"Recibimos una pregunta: {pregunta}")
            if pregunta == "Tarea":
                respuesta = choice(self.respuestas)
                self.send(respuesta, client_socket)
                print("Pregunta respondida al estudiante")
            
            elif pregunta == "Pregunta Dificil":
                # Pedir respuesta al profesor
                URL = "http://localhost:4444/respuesta"
                respuesta = requests.get(URL)
                status = respuesta.status_code
                print(f"CONSULTA AL PROFESOR: {status}")
                print(respuesta.json())
                self.send(respuesta.json()["texto"], client_socket)

                          

if __name__ == "__main__":
    port = 8080
    host = 'localhost'
    server = Tareo(port, host)