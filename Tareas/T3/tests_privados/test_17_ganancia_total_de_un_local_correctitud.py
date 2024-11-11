import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import ganancia_total_de_un_local



class TestGananciaTotalDeUnLocalCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que el test funcione si es que el local no tiene pedidos.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=9182,
            ),
            Pizza(
                nombre="Vegetariana_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=11585,
            ),
            Pizza(
                nombre="Hawaiiana_M",
                ingredientes="piña;jamón;queso;salsa de tomate",
                precio=10345,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=12845,
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.12
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.23
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.12
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.56
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=4, id_cliente=1, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=5, id_cliente=2, fecha="2021-01-01", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=3, fecha="2021-01-01", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=4, id_cliente=4, fecha="2021-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=3, id_cliente=5, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado_pedidos = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = ganancia_total_de_un_local(
            generador_entregado_contenido_pedidos,
            generador_entregado_pedidos,
            generador_entregado_pizzas,
            2,
        )

        resultado_esperado = 0

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que el test funcione si es que el local tiene 3 pedidos con más de una pizza y descuentos.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=8582,
            ),
            Pizza(
                nombre="Vegetariana_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=11285,
            ),
            Pizza(
                nombre="Hawaiiana_M",
                ingredientes="piña;jamón;queso;salsa de tomate",
                precio=12045,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=12645,
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=1, nombre="Vegetariana_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.32
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.32
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.32
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.44
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.44
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.05
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.5
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=21, id_cliente=1, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=2, fecha="2021-01-01", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=31, id_cliente=3, fecha="2021-01-01", hora="17:30:00"
            ),
            Pedido(
                id_pedido=4, id_local=11, id_cliente=4, fecha="2021-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=61, id_cliente=5, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado_pedidos = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = ganancia_total_de_un_local(
            generador_entregado_contenido_pedidos,
            generador_entregado_pedidos,
            generador_entregado_pizzas,
            1,
        )

        resultado_esperado = 19224

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que el test funcione si es que el local tiene 4 pedidos con más de una pizza y descuentos.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=8192,
            ),
            Pizza(
                nombre="Vegetariana_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=12385,
            ),
            Pizza(
                nombre="Hawaiiana_M",
                ingredientes="piña;jamón;queso;salsa de tomate",
                precio=12355,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=13345,
            ),
            Pizza(
                nombre="Napolitana_S",
                ingredientes="tomate;queso;aceitunas;orégano",
                precio=12515,
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=3, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=1, nombre="Vegetariana_M", cantidad=10, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepperoni Clásica_M", cantidad=8, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=6, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=2, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.14
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Hawaiiana_M", cantidad=2, descuento=0.14
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.40
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=2, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=9, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Napolitana_S", cantidad=6, descuento=0.6
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=12, id_cliente=1, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=2, fecha="2021-01-01", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=13, id_cliente=3, fecha="2021-01-01", hora="17:30:00"
            ),
            Pedido(
                id_pedido=4, id_local=5, id_cliente=4, fecha="2021-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=6, id_cliente=5, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=11, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado_pedidos = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = ganancia_total_de_un_local(
            generador_entregado_contenido_pedidos,
            generador_entregado_pedidos,
            generador_entregado_pizzas,
            1,
        )

        resultado_esperado = 35341

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que el test funcione si hay 5 pedidos en el local.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=8142,
            ),
            Pizza(
                nombre="Vegetariana_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=11382,
            ),
            Pizza(
                nombre="Hawaiiana_M",
                ingredientes="piña;jamón;queso;salsa de tomate",
                precio=12645,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=13345,
            ),
            Pizza(
                nombre="Margarita_S",
                ingredientes="tomate;queso;salsa de tomate",
                precio=9650,
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=1, nombre="Vegetariana_M", cantidad=12, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.34
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.34
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=6, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=2, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.34
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.34
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.34
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=6, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Margarita_S", cantidad=4, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Margarita_S", cantidad=23, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Vegetariana_M", cantidad=32, descuento=0.6
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=13, id_cliente=1, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=2, fecha="2021-01-01", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=3, id_cliente=3, fecha="2021-01-01", hora="17:30:00"
            ),
            Pedido(
                id_pedido=4, id_local=12, id_cliente=4, fecha="2021-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=9, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=7, id_local=8, id_cliente=7, fecha="2021-01-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=8, id_local=1, id_cliente=8, fecha="2021-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado_pedidos = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = ganancia_total_de_un_local(
            generador_entregado_contenido_pedidos,
            generador_entregado_pedidos,
            generador_entregado_pizzas,
            1,
        )

        resultado_esperado = 247254

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que el test funcione si hay 6 pedidos en el local.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=8192,
            ),
            Pizza(
                nombre="Vegetariana_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=12385,
            ),
            Pizza(
                nombre="Hawaiiana_M",
                ingredientes="piña;jamón;queso;salsa de tomate",
                precio=12445,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=12365,
            ),
            Pizza(
                nombre="Margarita_S",
                ingredientes="tomate;queso;salsa de tomate",
                precio=9150,
            ),
            Pizza(
                nombre="Napolitana_S",
                ingredientes="tomate;queso;aceitunas;orégano",
                precio=13505,
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=10, descuento=0.1
            ),
            ContenidoPedido(
                id_pedido=1, nombre="Vegetariana_M", cantidad=3, descuento=0.1
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.23
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.23
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=6, descuento=0.23
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.20
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.20
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=6, descuento=0.26
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=2, descuento=0.26
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=2, descuento=0.26
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Margarita_S", cantidad=14, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Margarita_S", cantidad=43, descuento=0.06
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Vegetariana_M", cantidad=2, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Napolitana_S", cantidad=15, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Napolitana_S", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Margarita_S", cantidad=1, descuento=0.2
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=31, id_cliente=2, fecha="2021-01-01", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=3, id_cliente=3, fecha="2021-01-01", hora="17:30:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=4, fecha="2021-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=12, id_cliente=5, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=14, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=7, id_local=1, id_cliente=7, fecha="2021-01-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=8, id_local=32, id_cliente=8, fecha="2021-01-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=9, id_local=2, id_cliente=9, fecha="2021-01-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=10,
                id_local=1,
                id_cliente=10,
                fecha="2021-01-01",
                hora="13:00",
            ),
        ]

        generador_entregado_pedidos = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = ganancia_total_de_un_local(
            generador_entregado_contenido_pedidos,
            generador_entregado_pedidos,
            generador_entregado_pizzas,
            1,
        )

        resultado_esperado = 603578

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)
