import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from utilidades import N_SECOND

from consultas import pizza_del_mes



class TestPizzaDelMesCorrectitud(unittest.TestCase):

    def shortDescription(self):

        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que el test funcione si es que que no hay pedidos en ese mes
        """
        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-01", hora="12:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=2, fecha="2021-01-01", hora="12:30"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=3, fecha="2021-01-01", hora="17:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=4, fecha="2021-01-01", hora="18:30"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2021-01-01", hora="12:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00"
            ),
        ]

        generador_entregado_pedidos = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
        ]

        generador_entregado_contenido_pedidos = (pedido for pedido in lista_entregada)

        resultado_estudiante = pizza_del_mes(
            generador_entregado_pedidos, generador_entregado_contenido_pedidos, "02"
        )

        self.assertIsInstance(resultado_estudiante, Iterable)

        resultado_esperado = []

        resultado_estudiante = list(resultado_estudiante)

        self.assertCountEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que el test funcione en el caso que haya dos pizzas empatadas en ventas
        """
        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-01", hora="12:00"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=3, fecha="2021-01-01", hora="17:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2021-01-01", hora="12:00"
            ),
        ]

        generador_entregado_pedidos = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=1, nombre="Margarita_S", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Margarita_M", cantidad=4, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Pepperoni Clásica_M", cantidad=5, descuento=0.0
            ),
        ]

        generador_entregado_contenido_pedidos = (pedido for pedido in lista_entregada)

        resultado_estudiante = pizza_del_mes(
            generador_entregado_pedidos, generador_entregado_contenido_pedidos, "01"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado_esperado = ["Pepperoni Clásica", "Margarita"]

        resultado_estudiante = list(resultado_estudiante)

        self.assertCountEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que el test funcione en caso de pizzas similares.
        """
        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-01", hora="12:00"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=3, fecha="2021-01-01", hora="17:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2021-01-01", hora="12:00"
            ),
        ]

        generador_entregado_pedidos = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=1, nombre="Margarita_S", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Margaritau_M", cantidad=14, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Margarita_M", cantidad=4, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Pepperoni Clásica_M", cantidad=10, descuento=0.0
            ),
        ]

        generador_entregado_contenido_pedidos = (pedido for pedido in lista_entregada)

        resultado_estudiante = pizza_del_mes(
            generador_entregado_pedidos, generador_entregado_contenido_pedidos, "01"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado_esperado = ["Pepperoni Clásica"]

        resultado_estudiante = list(resultado_estudiante)

        self.assertCountEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que el test funcione en casos más complejos con más de una pizza por pedido.
        """
        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-01", hora="12:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=2, fecha="2021-01-01", hora="12:30"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=3, fecha="2021-01-01", hora="17:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=4, fecha="2021-01-01", hora="18:30"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2021-01-01", hora="12:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00"
            ),
            Pedido(
                id_pedido=7, id_local=1, id_cliente=1, fecha="2021-02-01", hora="12:00"
            ),
            Pedido(
                id_pedido=8, id_local=1, id_cliente=2, fecha="2021-02-01", hora="12:30"
            ),
            Pedido(
                id_pedido=9, id_local=1, id_cliente=3, fecha="2021-02-01", hora="17:00"
            ),
            Pedido(
                id_pedido=10, id_local=1, id_cliente=4, fecha="2021-02-01", hora="18:30"
            ),
            Pedido(
                id_pedido=11, id_local=1, id_cliente=5, fecha="2021-02-01", hora="12:00"
            ),
            Pedido(
                id_pedido=12, id_local=1, id_cliente=6, fecha="2021-02-01", hora="13:00"
            ),
            Pedido(
                id_pedido=13, id_local=1, id_cliente=1, fecha="2021-03-01", hora="12:00"
            ),
        ]

        generador_entregado_pedidos = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=1, nombre="Margarita_S", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Hawaiiana_M", cantidad=4, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Pepperoni Clásica_M", cantidad=6, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Margarita_S", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Vegetariana_M", cantidad=3, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Hawaiiana_M", cantidad=4, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Pepperoni Clásica_M", cantidad=6, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Margarita_S", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Vegetariana_M", cantidad=3, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Hawaiiana_M", cantidad=4, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Pepperoni Clásica_M", cantidad=6, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=11, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=11, nombre="Margarita_M", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=12, nombre="Vegetariana_M", cantidad=3, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=12, nombre="Hawaiiana_M", cantidad=4, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=12, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=12, nombre="Pepperoni Clásica_M", cantidad=6, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=13, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.0
            ),
        ]

        generador_entregado_contenido_pedidos = (pedido for pedido in lista_entregada)

        resultado_estudiante = pizza_del_mes(
            generador_entregado_pedidos, generador_entregado_contenido_pedidos, "02"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado_esperado = ["Pepperoni Clásica"]

        resultado_estudiante = list(resultado_estudiante)

        self.assertCountEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que el test funcione en un caso normal.
        """
        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-01", hora="12:00"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=3, fecha="2021-01-01", hora="17:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2021-01-01", hora="12:00"
            ),
            Pedido(
                id_pedido=7, id_local=1, id_cliente=1, fecha="2021-02-01", hora="12:00"
            ),
            Pedido(
                id_pedido=8, id_local=1, id_cliente=2, fecha="2021-02-01", hora="12:30"
            ),
        ]

        generador_entregado_pedidos = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=1, nombre="Margarita_S", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Margarita_M", cantidad=4, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Pepperoni Clásica_M", cantidad=10, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Pepperoni Clásica_M", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Pepperoni Clásica_M", cantidad=10, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Margarita_S", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Vegetariana_M", cantidad=3, descuento=0.0
            ),
        ]

        generador_entregado_contenido_pedidos = (pedido for pedido in lista_entregada)

        resultado_estudiante = pizza_del_mes(
            generador_entregado_pedidos, generador_entregado_contenido_pedidos, "01"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado_esperado = ["Pepperoni Clásica"]

        resultado_estudiante = list(resultado_estudiante)

        self.assertCountEqual(resultado_estudiante, resultado_esperado)
