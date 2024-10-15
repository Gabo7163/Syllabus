import socket
import threading
import requests

class Docencia:
    def __init__(self, host: str, port: int, datos_otro_cliente: dict) -> None:
        print("Inicializando cliente P2P (2)...")
        self.host = host
        self.port = port
        self.datos_otro_cliente = datos_otro_cliente

        self.sockets = {
            'server': socket.socket(socket.AF_INET, socket.SOCK_STREAM),
            'client': socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        }

        self.bind_and_listen()
        self.accept_connections()

        try:
            self.connect_to_server()
        except ConnectionError:
            print("Conexión terminada.")
            self.sockets['client'].close()
            exit()

    def bind_and_listen(self) -> None:
        self.sockets['server'].bind((self.host, self.port))
        self.sockets['server'].listen()
        print(f"Cliente P2P (2) escuchando en {self.host}:{self.port}...")

    def accept_connections(self) -> None:
        thread = threading.Thread(target=self.accept_connections_thread)
        thread.start()

    def accept_connections_thread(self) -> None:
        while True:
            client_socket, _ = self.sockets['server'].accept()
            threading.Thread(
                target=self.listen_client_thread,
                args=(client_socket,),
                daemon=True
            ).start()

    def listen_client_thread(self, client_socket: socket.socket) -> None:
        while True:
            try:
                response_bytes_length = client_socket.recv(4)
                response_length = int.from_bytes(response_bytes_length, byteorder='big')
                pregunta = client_socket.recv(response_length).decode()

                print(f"Recibimos una pregunta: {pregunta}")

                if pregunta == "Contenido":
                    self.answer_client("Docencio: respondiendo pregunta de contenido", client_socket)
                else:
                    threading.Thread(
                        target=self.procesar_pregunta_tareo,
                        args=(pregunta, client_socket),
                        daemon=True
                    ).start()

            except ConnectionResetError:
                print("Conexión con el cliente cerrada.")
                break

    def procesar_pregunta_tareo(self, pregunta: str, client_socket: socket.socket) -> None:
        # Consultar a Tareo y responder al cliente
        respuesta = self.consultar_a_tareo(pregunta)
        self.answer_client(f"Respuesta del Tareo o Profesor: {respuesta}", client_socket)
        self.notificar_profesor()

    def answer_client(self, value: str, sock: socket.socket) -> None:
        msg_bytes = value.encode()
        sock.sendall(len(msg_bytes).to_bytes(4, byteorder='big') + msg_bytes)

    def connect_to_server(self) -> None:
        self.sockets['client'].connect(
            (self.datos_otro_cliente['host'], self.datos_otro_cliente['port'])
        )
        print("Cliente conectado exitosamente al otro cliente.")


    def consultar_a_tareo(self, pregunta: str) -> str:
        self.send(pregunta)
        response = self.sockets['client'].recv(4096).decode()
        return response

    def send(self, msg: str) -> None:
        msg_bytes = msg.encode()
        self.sockets['client'].sendall(len(msg_bytes).to_bytes(4, byteorder='big') + msg_bytes)

    def notificar_profesor(self) -> None:
        try:
            response = requests.post("http://localhost:4444/preguntas")
            if response.status_code == 200:
                print(f"Contador de preguntas actualizado: {response.json()['texto']}")
        except requests.RequestException as e:
            print(f"Error al conectar con el profesor: {e}")


if __name__ == "__main__":
    host = 'localhost'
    port = 8081
    datos_otro_cliente = {'port': 8080, 'host': 'localhost'}
    client = Docencia(host, port, datos_otro_cliente)