import socket
import threading
import pickle
import sys
import os
from typing import List


class Mensaje:
    """
        Esta clase empaqueta los mensajes que serán enviados entre conexiones.
    """

    def __init__(self, operacion=None, data=None, estado=None) -> None:
        # Guarda el tipo de operación: listar o descargar
        self.operacion = operacion
        # Guarda la información necesaria según la consulta
        self.data = data
        # Guarda el resultado de la consulta "ok" o "error"
        self.estado = estado


class Servidor:
    """
        Clase que representa un servidor distribuidor de archivos.
        En cuanto se instancia levanta un socket para escuchar potenciales
        clientes.
    """
    id_clientes = 0

    def __init__(self, port: int, host: str) -> None:
        '''
        Inicializar el servidor.

        PARTE 1: Debemos instanciar un socket para que sea servidor y pueda escuchar conexiones.
        '''
        self.chunk_size = 2**16
        self.host = host
        self.port = port
        self.sockets = {}

        # Completar...

    def bind_listen(self) -> None:
        '''
        Método que conecta el servidor al host y port dado.

        PARTE 2: ¿Por qué este método lanza error?
        '''

        # Aquí hay 1 error. Además, el método está incompleto.
        self.socket_server.connect((self.host, self.port))
        print(f"Servidor escuchando en {self.host} : {self.port}")

    def accept_connections(self) -> None:
        '''
        Método encargado de aceptar conexiones de clientes.

        PARTE 3: Debe poder aceptar múltiples conexiones, y además no bloquear al hilo principal
        para poder hacer otras cosas en el server si se necesita.
        '''
        socket_cliente, address = self.socket_server.accept()
        print(f"Nuevo cliente conectado: {socket_cliente} {address}")

    def accept_connections_thread(self) -> None:
        '''
        ¿Para qué servirá esta funcion auxiliar?
        '''
        while True:
            socket_cliente, address = self.socket_server.accept()
            print(f"Nuevo cliente conectado:", socket_cliente, address)

            # ¿Por qué hacemos esto?
            self.sockets[self.id_clientes] = {
                "socket": socket_cliente,
                "address": address,
            }

            listening_client_thread = threading.Thread(
                target=self.listen_client_thread, args=(
                    self.id_clientes, socket_cliente,), daemon=True
            )
            self.id_clientes += 1
            listening_client_thread.start()

    def recibir_bytes(self, socket_cliente: socket, cantidad: int) -> bytearray:
        '''
        Este método de recibir bytes desde el cliente hasta completar una cantidad
        específica, y pasarlos a un bytearray.

        PARTE 4: Completar el método para hacer lo anterior.
        '''
        bytes_leidos = bytearray()
        while len(bytes_leidos) < cantidad:
            # agregamos los bytes de a poco...
            pass

    def listen_client_thread(self, id_cliente: int, socket_cliente: socket) -> None:
        '''
        Este método se encarga de seguir el protocolo para decodificar el mensaje recibido.

        PARTE 5: Completar este método con todo lo que falta para decodificar el mensaje
        y pasarlo al método manejar_mensaje.
        '''
        while True:
            print(
                f"Cliente [{id_cliente}] Recibiendo largo del siguiente mensaje"
            )

            # Recibamos primero el largo del mensaje:
            largo_mensaje = None

            print(
                f"Cliente [{id_cliente}] Recibiendo mensaje de largo {largo_mensaje}"
            )

            # Ahora sabiendo el largo, recibamos el mensaje en sí:
            bytes_mensaje = None

            print(
                f"Cliente [{id_cliente}] Mensaje de largo {largo_mensaje} recibido"
            )

            # Con el mensaje recibido, intentemos deserializarlo
            # y entregarlo al método manejar_mensaje. Recuerda manejar errores.

    def manejar_mensaje(self, mensaje: Mensaje, id_cliente: int) -> None:
        """
        Maneja el comando obtenido y realiza la acción acorde.

        Al programar el flujo, toma en cuenta:
        ¿De donde sacamos el comando enviado?
        Si queremos descargar un archivo, ¿como el servidor sabrá cuál archivo enviar?
        ¿Qué pasa si el servidor no tiene el archivo pedido?
        """
        if mensaje.operacion == "listar":
            respuesta = Mensaje(data=self.listar_archivos(), estado="ok")
            self.enviar_mensaje(respuesta, id_cliente)
        elif mensaje.operacion == "descargar":
            nombre_archivo = mensaje.data
            if (
                nombre_archivo in self.listar_archivos()
            ):  # También usar os.path.exists()
                self.enviar_archivo(nombre_archivo, id_cliente)
            else:
                respuesta = Mensaje(estado="error")
                self.enviar_mensaje(respuesta, id_cliente)

    def enviar_mensaje(self, mensaje: Mensaje, id_cliente: int) -> None:
        '''
        Envia mensajes al cliente siguiendo el protocolo pedido.

        PARTE 6: Debe enviar el mensaje cumpliendo con las reglas antes mencionadas:
        Primero enviar 4 bytes con el largo del mensaje, y luego el mensaje.

        Este método tiene 1 error y 1 detalle no del todo correcto. ¡Son dificiles de encontrar!
        '''

        # Dejamos este print para que veas cómo se ve un mensaje. Luego se puede borrar.
        print(mensaje.__dict__)
        print(f"[Cliente {id_cliente}] Enviando {mensaje}")
        bytes_mensaje = pickle.dump(mensaje)
        largo_mensaje = len(bytes_mensaje).to_bytes(4, "big")
        mensaje_total = largo_mensaje + bytes_mensaje
        self.sockets[id_cliente]['socket'].sendall(mensaje_total)
        print(f"[Cliente {id_cliente}] {mensaje} enviado")

    def enviar_archivo(self, archivo: str, id_cliente: int) -> None:
        """
        Este método debe poder enviar un archivo al socket del cliente

        PARTE 7: Completar el método.
        """

        pass

    def listar_archivos(self) -> List[str]:
        return os.listdir("archivos")


if __name__ == "__main__":
    # Recibimos el puerto y host por consola, pero si no llega damos valores
    # por defecto.
    PORT = 3247 if len(sys.argv) < 2 else int(sys.argv[1])
    HOST = "localhost" if len(sys.argv) < 3 else sys.argv[2]
    """
    Ahora podemos ejecutar el archivo de la siguientes 3 formas:
     - python3 servidor.py
     - python3 servidor.py 7584 
     - python3 servidor.py 4113 localhost

    OJO: recordar que el puerto debemos pasarlo siempre como int, no str.
    """
    server = Servidor(PORT, HOST)

    input('Presione enter para cerrar')
    server.socket_server.close()
    exit(1)
