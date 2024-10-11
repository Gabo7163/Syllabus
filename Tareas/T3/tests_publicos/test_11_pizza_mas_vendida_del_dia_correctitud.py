import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from utilidades import N_SECOND

from consultas import pizza_mas_vendida_del_dia



class TestPizzaMasVendidaDelDiaCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica funcionamiento correcto cuando en el día determinado no hay ventas de pizzas.
        """
        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=4, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_XL", cantidad=10, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana Normal_M", cantidad=6, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="El Pepe Hawaiiana_M", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones bajo ajo_S", cantidad=30, descuento=0.0
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-29", hora="12:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=2, fecha="2021-04-05", hora="12:30"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=3, fecha="2021-05-07", hora="17:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=4, fecha="2022-02-03", hora="18:30"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2010-01-01", hora="12:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00"
            ),
        ]

        generador_entregado_asociaciones = (
            asociacion for asociacion in lista_entregada
        )

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_entregado_pedidos, generador_entregado_asociaciones, "2022-02-04"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pizza for pizza in resultado_estudiante]

        lista_esperada = []

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica funcionamiento correcto cuando solamente una pizza se vende más que el resto de pizzas en el día.
        """
        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=40000, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_XL", cantidad=20, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana Normal_M", cantidad=450, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepe Le Hawaiiana_M", cantidad=80, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones bajo ajo_S", cantidad=1, descuento=0.0
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-29", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=2, fecha="2010-01-01", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=3, fecha="2021-05-07", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=4, fecha="2010-01-01", hora="18:30:00"
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

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_entregado_pedidos, generador_entregado_asociaciones, "2010-01-01"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pizza for pizza in resultado_estudiante]

        lista_esperada = ["Pepe Le Hawaiiana"]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica funcionamiento correcto cuando hay un empate en cantidad de pizzas vendidas en dos pizzas distintas.
        """
        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1,
                nombre="Pepperoni ULTRA Clásica_XL",
                cantidad=50,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=2,
                nombre="Pepperoni MEGA Clásica_XL",
                cantidad=50,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana Normal_M", cantidad=50, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepe Hawaiiana_M", cantidad=50, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5,
                nombre="Camarones bajo no ajo (T3 CANON EDITION)_S",
                cantidad=50,
                descuento=0.0,
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-29", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=2, fecha="2010-01-01", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=3, fecha="2021-05-07", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=4, fecha="2010-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2021-01-29", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-30", hora="13:00:00"
            ),
        ]

        generador_entregado_asociaciones = (
            asociacion for asociacion in lista_entregada
        )

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_entregado_pedidos, generador_entregado_asociaciones, "2021-01-29"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pizza for pizza in resultado_estudiante]

        lista_esperada = [
            "Pepperoni ULTRA Clásica",
            "Camarones bajo no ajo (T3 CANON EDITION)",
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica funcionamiento correcto cuando hay un empate en cantidad de pizzas vendidas en tres o más pizzas distintas, y hay pizzas con el mismo nombre pero distinto tamaño.
        """
        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1,
                nombre="Pepperoni Clásica_XL",
                cantidad=2,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=2,
                nombre="Pepperoni Clásica_XL",
                cantidad=347,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=3, nombre="2578917_M", cantidad=49, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="2578917_XL", cantidad=299, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5,
                nombre="Camarones CLASIC bajo no ajo_S",
                cantidad=349,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=6,
                nombre="Napolitan bajo no KANNON ajo_XL",
                cantidad=100,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=7,
                nombre="Hawaiana no SHANNON ajo_L",
                cantidad=349,
                descuento=0.0,
            ),
            ContenidoPedido(id_pedido=8, nombre="2578917_S", cantidad=1, descuento=0.0),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-29", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=2, fecha="2021-05-07", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=3, fecha="2021-05-07", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=4, fecha="2021-05-07", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2021-05-07", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-05-07", hora="13:00:00"
            ),
            Pedido(
                id_pedido=7, id_local=1, id_cliente=7, fecha="2021-05-07", hora="14:00:00"
            ),
            Pedido(
                id_pedido=8, id_local=1, id_cliente=8, fecha="2021-05-07", hora="15:00:00"
            ),
        ]

        generador_entregado_asociaciones = (
            asociacion for asociacion in lista_entregada
        )

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_entregado_pedidos, generador_entregado_asociaciones, "2021-05-07"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pizza for pizza in resultado_estudiante]

        lista_esperada = [
            "Hawaiana no SHANNON ajo",
            "Camarones CLASIC bajo no ajo",
            "2578917",
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)
