import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_15 import *
from utilidades import N_SECOND

from consultas import pizza_favorita_cliente



class TestPizzaFavoritaClienteCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica funcionamiento correcto cuando el cliente no haya comprado ninguna pizza.
        """
        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-29", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=1, fecha="2021-04-05", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=3, fecha="2021-05-07", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=4, fecha="2022-02-03", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2010-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado_asociaciones = (
            asociacion for asociacion in lista_entregada
        )

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1,
                nombre="Pepperoni Automata Clásica_M",
                cantidad=4,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=2,
                nombre="Pepperoni Automata Clásica_XL",
                cantidad=10,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=3,
                nombre="Vegetariana KNOX Normal_M",
                cantidad=6,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=4, nombre="The END is Near_M", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="CONcat DECALOGUE ajo_S", cantidad=30, descuento=0.0
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        resultado_estudiante = pizza_favorita_cliente(
            generador_entregado_asociaciones, generador_entregado_pedidos, 2
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [tupla for tupla in resultado_estudiante]

        lista_esperada = []

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica funcionamiento correcto cuando el cliente solo tiene una pizza que compró más, y siempre del mismo tamaño.
        """
        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-29", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=2, fecha="2021-04-05", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=3, fecha="2021-05-07", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=4, fecha="2022-02-03", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2010-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=7, id_local=1, id_cliente=1, fecha="2023-05-05", hora="12:30:00"
            ),
        ]

        generador_entregado_asociaciones = (
            asociacion for asociacion in lista_entregada
        )

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1,
                nombre="Pepperoni NOT Clásica_M",
                cantidad=20,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_XL", cantidad=10, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana Normal_M", cantidad=6, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepe de Hawaiiana_M", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones bajo ajo_S", cantidad=30, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Pepperoni Clásica_M", cantidad=24, descuento=0.0
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        resultado_estudiante = pizza_favorita_cliente(
            generador_entregado_asociaciones, generador_entregado_pedidos, 1
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [tupla for tupla in resultado_estudiante]

        lista_esperada = [("Pepperoni Clásica", 24)]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica funcionamiento correcto cuando el cliente solo tiene una pizza que compró más, pero en distintos tamaños (evaluar la suma por los diferentes tamaños).
        """
        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-29", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=1, fecha="2021-04-05", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=1, fecha="2021-05-07", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=4, fecha="2022-02-03", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=1, fecha="2010-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=7, id_local=1, id_cliente=1, fecha="2023-05-05", hora="12:30:00"
            ),
            Pedido(
                id_pedido=8, id_local=1, id_cliente=1, fecha="2023-08-05", hora="12:35:00"
            ),
        ]

        generador_entregado_asociaciones = (
            asociacion for asociacion in lista_entregada
        )

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1,
                nombre="Pepperoni NOT Clásica_M",
                cantidad=21,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=2,
                nombre="Pepperoni Mega Clásica_S",
                cantidad=11,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana Normal_M", cantidad=26, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepe de Hawaiiana_M", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones bajo ajo_S", cantidad=30, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=7,
                nombre="Pepperoni Mega Clásica_M",
                cantidad=16,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=8,
                nombre="Pepperoni Mega Clásica_XL",
                cantidad=10,
                descuento=0.0,
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        resultado_estudiante = pizza_favorita_cliente(
            generador_entregado_asociaciones, generador_entregado_pedidos, 1
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [tupla for tupla in resultado_estudiante]

        lista_esperada = [("Pepperoni Mega Clásica", 37)]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica funcionamiento correcto cuando el cliente tiene dos pizzas distintas que haya comprado la misma cantidad de veces.
        """
        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=4, fecha="2021-01-29", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=4, fecha="2021-04-05", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=4, fecha="2021-05-07", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=2, fecha="2022-02-03", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=4, fecha="2010-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=7, id_local=1, id_cliente=4, fecha="2023-05-05", hora="12:30:00"
            ),
            Pedido(
                id_pedido=8, id_local=1, id_cliente=4, fecha="2023-08-05", hora="12:35:00"
            ),
        ]

        generador_entregado_asociaciones = (
            asociacion for asociacion in lista_entregada
        )

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1,
                nombre="Pepperoni NOT Clásica_M",
                cantidad=21,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=2,
                nombre="Pepperoni Mega Clásica_S",
                cantidad=11,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana Normal_M", cantidad=5000, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepe de Hawaiiana_M", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones bajo ajo_S", cantidad=5000, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=7,
                nombre="Pepperoni Mega Clásica_M",
                cantidad=16,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=8,
                nombre="Pepperoni Mega Clásica_XL",
                cantidad=10,
                descuento=0.0,
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        resultado_estudiante = pizza_favorita_cliente(
            generador_entregado_asociaciones, generador_entregado_pedidos, 4
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [tupla for tupla in resultado_estudiante]

        lista_esperada = [("Camarones bajo ajo", 5000),
                          ("Vegetariana Normal", 5000)]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica funcionamiento correcto cuando el cliente tiene tres o más pizzas distintas que haya comprado la misma cantidad de veces.
        """
        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=4, fecha="2021-01-29", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=4, fecha="2021-04-05", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=4, fecha="2021-05-07", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=2, fecha="2022-02-03", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=4, fecha="2010-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=7, id_local=1, id_cliente=4, fecha="2023-05-05", hora="12:30:00"
            ),
            Pedido(
                id_pedido=8, id_local=1, id_cliente=4, fecha="2023-08-05", hora="12:35:00"
            ),
        ]

        generador_entregado_asociaciones = (
            asociacion for asociacion in lista_entregada
        )

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1,
                nombre="Pepperoni NOT Clásica_XL",
                cantidad=7000,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=2,
                nombre="Pepperoni NOT Clásica_S",
                cantidad=9,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=3,
                nombre="Vegetariana FNormal_M",
                cantidad=7009,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepe de Hawaiiana_M", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones CON ajo_S", cantidad=7009, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=7,
                nombre="Pepperoni Mega Clásica_M",
                cantidad=16,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=8,
                nombre="Pepperoni Mega Clásica_XL",
                cantidad=10,
                descuento=0.0,
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        resultado_estudiante = pizza_favorita_cliente(
            generador_entregado_asociaciones, generador_entregado_pedidos, 4
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [tupla for tupla in resultado_estudiante]

        lista_esperada = [
            ("Pepperoni NOT Clásica", 7009),
            ("Vegetariana FNormal", 7009),
            ("Camarones CON ajo", 7009),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)
