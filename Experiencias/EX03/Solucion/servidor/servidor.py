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
        # Creamos el servidor
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Luego hacer bind, listen y aceptar conexiones de usuarios
        self.bind_listen()
        self.accept_connections()

    def bind_listen(self) -> None:
        '''
        Método que conecta el servidor al host y port dado.

        PARTE 2: ¿Por qué este método lanza error?
        '''

        # Error: se usa el método connect y no bind. Connect es para el cliente.
        # Luego todavía falta habilitar el socket para escuchar.
        # por eso hacemos listen y ponemos el print que queremos
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen()
        print(f"Servidor escuchando en {self.host} : {self.port}")

    def accept_connections(self) -> None:
        '''
        Método encargado de aceptar conexiones de clientes.

        PARTE 3: Debe poder aceptar múltiples conexiones, y además no bloquear al hilo principal
        para poder hacer otras cosas en el server si se necesita.
        '''

        # Podemos decir que este thread es nuestro "portero"
        # que se encarga de abrir la puerta a cada cliente
        thread = threading.Thread(
            target=self.accept_connections_thread, daemon=True)
        thread.start()
        """
        Aclaración: el thread debe ser daemon para que, deseamos cerrar el programa,
        este thread sea detenido y eliminado. En otro caso, el programa deberá esperar
        a que el thread finalice para poder finalizar su ejecución.

        Importante: No es necesario guardar un thread en memoria, sea
        o no daemon. No obstante, el único problema
        es que el servidor no tendrá forma de acceder al thread para, por ejemplo, hacerle stop()
        """

    def accept_connections_thread(self) -> None:
        '''
        ¿Para qué servirá esta funcion auxiliar?
        '''

        """
        Comentario: Se debe inicializar un hilo para escuchar a dicho cliente.
        Esto se debe hacer en un hilo paralelo para no bloquear otras funciones
        del servidor.
        ------
        Eternamente el thread escucha posibles sockets que quieran
        conectarse, guarda su dirección en un diccionario y crea otro thread
        encargado de escuchar únicamente a ese nuevo cliente.
        Podemos decir que nuestro "portero" está  atento a abrir la puerta
        a cada cliente y crea un nuevo encargado de escuchar constantemente
        al nuevo cliente.
        """

        while True:
            socket_cliente, address = self.socket_server.accept()
            print(f"Nuevo cliente conectado: {socket_cliente} {address}")

            # Siempre se recomienda guardar la info del cliente para fácil acceso
            # (administrar clientes, cortar conexiones, etc.)
            self.sockets[self.id_clientes] = {
                "socket": socket_cliente,
                "address": address,
            }

            # Creamos nuestro "minion" encargado de escuchar exclusivamente al cliente
            # también es daemon para poder detener el thread si es que el servidor
            # desea finalizar su ejecución.
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
            cantidad_restante = cantidad - len(bytes_leidos)
            bytes_leer = min(self.chunk_size, cantidad_restante)
            # Importante recv(N) va a leer hasta N bytes que le manden. Si le mandan
            # menos, por ejemplo, K (con K < N) entonces respuesta será de largo K
            respuesta = socket_cliente.recv(bytes_leer)
            if len(respuesta) < bytes_leer:
                # Si me llega más chico de lo esperado, algo pasó con el cliente,
                # retorno lo que llevo para intentar ver el mensaje
                return bytes_leidos
            bytes_leidos.extend(respuesta)
        return bytes_leidos

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
            bytes_mensaje_parte_1 = self.recibir_bytes(socket_cliente, 4)
            largo_mensaje = int.from_bytes(bytes_mensaje_parte_1, "big")
            print(
                f"Cliente [{id_cliente}] Recibiendo mensaje de largo {largo_mensaje}"
            )

            # Ahora sabiendo el largo, recibamos el mensaje en sí:
            bytes_mensaje_parte_2 = self.recibir_bytes(
                socket_cliente, largo_mensaje)
            print(
                f"Cliente [{id_cliente}] Mensaje de largo {largo_mensaje} recibido"
            )

            # Con el mensaje recibido, intentemos deserializarlo
            # y entregarlo al método manejar_mensaje. Recuerda manejar errores.
            if largo_mensaje == 0:
                # Mensaje de largo 0, se cerró el cliente de golpe
                print(f"Cliente [{id_cliente}] Cliente desconectado")
                del self.sockets[id_cliente]
                break
            try:
                mensaje = pickle.loads(bytes_mensaje_parte_2)
                self.manejar_mensaje(mensaje, id_cliente)
            except Exception:
                # En este caso, da lo mismo el tipo de error que ocurra, si el mensaje
                # del cliente provoca un error, se elimina su información y se deja de escuchar
                # de este modo el servidor sigue funcionando
                print(f"[{id_cliente}] Cliente desconectado")
                del self.sockets[id_cliente]
                break

    def manejar_mensaje(self, mensaje: Mensaje, id_cliente: int) -> None:
        """
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

        # Error 1: Usamos dump en vez de dumps, sin la "S" es para archivos.
        # Detalle: El mensaje se debería mandar en 2 rondas: primero un N de 4 bytes
        #          con el largo del mensaje y luego el mensaje.
        #   Solución: hacer 2 sendall.
        print(f"[Cliente {id_cliente}] Enviando {mensaje}")
        bytes_mensaje = pickle.dumps(mensaje)
        self.sockets[id_cliente]['socket'].sendall(
            len(bytes_mensaje).to_bytes(4, "big"))
        self.sockets[id_cliente]['socket'].sendall(bytes_mensaje)
        print(f"[Cliente {id_cliente}] {mensaje} enviado")
        """
        Observación: Si haces:
            todo_mensaje = len(bytes_mensaje).to_bytes(4, "big") + bytes_mensaje
            socket_cliente.sendall(todo_mensaje)

        No está mal, porque igual se está mandando primero 4 bytes con el largo y 
        luego el mensaje, pero es fácil que uno se equivoque y haga 
            socket_cliente.sendall(bytes_mensaje)
        Es decir, enviar solo el mensaje y nunca los primeros 4 bytes con el largo.
        Eso último estaría mal porque no sigue el protocolo y hace que el cliente
        no sepa cuánto esperar a recibir a futuro.
        """

    def enviar_archivo(self, archivo: str, id_cliente: int) -> None:
        """
        Este método debe poder enviar un archivo al socket del cliente

        PARTE 7: Completar el método.
        """
        with open(os.path.join("archivos", archivo), "rb") as file:
            bytes_archivo = file.read()
        respuesta = Mensaje(data=bytes_archivo, estado="ok")
        self.enviar_mensaje(respuesta, id_cliente)

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

    input("Presione enter para cerrar")
    server.socket_server.close()
    exit(1)
