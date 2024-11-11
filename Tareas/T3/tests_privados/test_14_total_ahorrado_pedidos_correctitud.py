import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import total_ahorrado_pedidos



class TestTotalAhorradoPedidosCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que el test funcione si es que no hay descuentos en los pedidos.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=11383,
            ),
            Pizza(
                nombre="Super Vegetariana_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas;salsa ranch",
                precio=11785,
            ),
            Pizza(
                nombre="Hawaiiana Maxima_M",
                ingredientes="piña;jamón;queso;salsa de tomate",
                precio=12355,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=12305,
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana Maxima_M", cantidad=4, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Super Vegetariana_M", cantidad=3, descuento=0.0
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        resultado_estudiante = total_ahorrado_pedidos(
            generador_entregado_contenido_pedidos, generador_entregado_pizzas
        )

        resultado_esperado = 0

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que el test funcione si es que se entrega un generador de pedidos vacío.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=8383,
            ),
            Pizza(
                nombre="Vegetariana_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=11395,
            ),
            Pizza(
                nombre="Hawaiiana_M",
                ingredientes="piña;jamón;queso;salsa de tomate",
                precio=12340,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=12395,
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

        lista_entregada = []

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        resultado_estudiante = total_ahorrado_pedidos(
            generador_entregado_contenido_pedidos, generador_entregado_pizzas
        )

        resultado_esperado = 0

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que el test funcione si todos los pedidos tienen descuentos.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=8189,
            ),
            Pizza(
                nombre="Vegetariana_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=11395,
            ),
            Pizza(
                nombre="Hawaiiana_M",
                ingredientes="piña;jamón;queso;salsa de tomate",
                precio=10345,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=19345,
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.1
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.35
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.7
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        resultado_estudiante = total_ahorrado_pedidos(
            generador_entregado_contenido_pedidos, generador_entregado_pizzas
        )

        resultado_esperado = 58576

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que el test funcione si algunos pedidos tienen descuentos y alguno más de una pizza.
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
                precio=11485,
            ),
            Pizza(
                nombre="Hawaiiana_M",
                ingredientes="piña;jamón;queso;salsa de tomate",
                precio=13345,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=12375,
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.25
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.08
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.24
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.10
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Camarones sobre ajo_S", cantidad=2, descuento=0.2
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        resultado_estudiante = total_ahorrado_pedidos(
            generador_entregado_contenido_pedidos, generador_entregado_pizzas
        )

        resultado_esperado = 28279

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    def test_4(self):
        """
        Verifica que el test funcione si la mayoría de los pedidos tienen descuento y alguno más de una pizza.
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
                precio=11355,
            ),
            Pizza(
                nombre="Hawaiiana_M",
                ingredientes="piña;jamón;queso;salsa de tomate",
                precio=12245,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=12347,
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
                id_pedido=4, nombre="Hawaiiana_M", cantidad=1, descuento=0.35
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.35
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.24
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.10
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.26
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        resultado_estudiante = total_ahorrado_pedidos(
            generador_entregado_contenido_pedidos, generador_entregado_pizzas
        )

        resultado_esperado = 41968

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)
