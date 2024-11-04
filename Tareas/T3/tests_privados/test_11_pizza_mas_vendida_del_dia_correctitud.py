import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from por_copiar.utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

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
                id_pedido=2, nombre="Pepperoni Clásica_XL", cantidad=15, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana NNormal_M", cantidad=6, descuento=0.0
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
                id_pedido=1,
                id_local=1,
                id_cliente=1,
                fecha="2021-01-29",
                hora="12:00:00",
            ),
            Pedido(
                id_pedido=2,
                id_local=1,
                id_cliente=2,
                fecha="2021-04-05",
                hora="12:30:00",
            ),
            Pedido(
                id_pedido=3,
                id_local=1,
                id_cliente=3,
                fecha="2021-05-07",
                hora="17:00:00",
            ),
            Pedido(
                id_pedido=4,
                id_local=1,
                id_cliente=4,
                fecha="2022-02-03",
                hora="18:30:00",
            ),
            Pedido(
                id_pedido=5,
                id_local=1,
                id_cliente=5,
                fecha="2010-01-07",
                hora="12:00:00",
            ),
            Pedido(
                id_pedido=6,
                id_local=1,
                id_cliente=6,
                fecha="2021-01-06",
                hora="13:00:00",
            ),
        ]

        generador_entregado_asociaciones = (
            asociacion for asociacion in lista_entregada
        )

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_entregado_pedidos, generador_entregado_asociaciones, "2022-01-01"
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
                id_pedido=4, nombre="Pepe Le Hawaiiana_M", cantidad=82, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5,
                nombre="Camarones bajo Sin ajo_L",
                cantidad=84,
                descuento=0.0,
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1,
                id_local=1,
                id_cliente=1,
                fecha="2021-01-29",
                hora="12:00:00",
            ),
            Pedido(
                id_pedido=2,
                id_local=1,
                id_cliente=2,
                fecha="2010-01-01",
                hora="12:30:00",
            ),
            Pedido(
                id_pedido=3,
                id_local=1,
                id_cliente=3,
                fecha="2021-05-07",
                hora="17:00:00",
            ),
            Pedido(
                id_pedido=4,
                id_local=1,
                id_cliente=4,
                fecha="2010-01-03",
                hora="18:30:00",
            ),
            Pedido(
                id_pedido=5,
                id_local=1,
                id_cliente=5,
                fecha="2010-01-03",
                hora="12:00:00",
            ),
            Pedido(
                id_pedido=6,
                id_local=1,
                id_cliente=6,
                fecha="2010-01-03",
                hora="13:00:00",
            ),
        ]

        generador_entregado_asociaciones = (
            asociacion for asociacion in lista_entregada
        )

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_entregado_pedidos, generador_entregado_asociaciones, "2010-01-03"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pizza for pizza in resultado_estudiante]

        lista_esperada = ["Camarones bajo Sin ajo"]

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
                cantidad=603,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=2,
                nombre="Pepperoni OMEGA Clásica_XL",
                cantidad=603,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana Normal_M", cantidad=50, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepel Hawaiiana_M", cantidad=603, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5,
                nombre="Camarones bajo no ajo (T3 CANON EDITION)_S",
                cantidad=603,
                descuento=0.0,
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1,
                id_local=1,
                id_cliente=1,
                fecha="2021-01-29",
                hora="12:00:00",
            ),
            Pedido(
                id_pedido=2,
                id_local=1,
                id_cliente=2,
                fecha="2010-01-01",
                hora="12:30:00",
            ),
            Pedido(
                id_pedido=3,
                id_local=1,
                id_cliente=3,
                fecha="2021-05-07",
                hora="17:00:00",
            ),
            Pedido(
                id_pedido=4,
                id_local=1,
                id_cliente=4,
                fecha="2010-01-01",
                hora="18:30:00",
            ),
            Pedido(
                id_pedido=5,
                id_local=1,
                id_cliente=5,
                fecha="2021-01-29",
                hora="12:00:00",
            ),
            Pedido(
                id_pedido=6,
                id_local=1,
                id_cliente=6,
                fecha="2021-01-30",
                hora="13:00:00",
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

        lista_esperada = [
            "Pepperoni OMEGA Clásica",
            "Pepel Hawaiiana",
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
                nombre="FURUDO_S",
                cantidad=700,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=3,
                nombre="PIZZA PIZZA_M",
                cantidad=1002,
                descuento=0.0,
            ),
            ContenidoPedido(id_pedido=2, nombre="ERIKA_L", cantidad=502, descuento=0.0),
            ContenidoPedido(
                id_pedido=4, nombre="ERIKA_XL", cantidad=500, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5,
                nombre="Camarones CLASIC bajo no ajo_S",
                cantidad=1001,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=6,
                nombre="FURUDO_M",
                cantidad=302,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=7,
                nombre="LOGIC_XL",
                cantidad=100,
                descuento=0.0,
            ),
            ContenidoPedido(id_pedido=8, nombre="LOGIC_M", cantidad=902, descuento=0.0),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1,
                id_local=1,
                id_cliente=1,
                fecha="2022-05-07",
                hora="12:00:00",
            ),
            Pedido(
                id_pedido=2,
                id_local=1,
                id_cliente=2,
                fecha="2022-05-07",
                hora="12:30:00",
            ),
            Pedido(
                id_pedido=3,
                id_local=1,
                id_cliente=3,
                fecha="2021-05-07",
                hora="17:00:00",
            ),
            Pedido(
                id_pedido=4,
                id_local=1,
                id_cliente=4,
                fecha="2022-05-07",
                hora="18:30:00",
            ),
            Pedido(
                id_pedido=5,
                id_local=1,
                id_cliente=5,
                fecha="2022-05-07",
                hora="12:00:00",
            ),
            Pedido(
                id_pedido=6,
                id_local=1,
                id_cliente=6,
                fecha="2022-05-07",
                hora="13:30:00",
            ),
            Pedido(
                id_pedido=7,
                id_local=1,
                id_cliente=7,
                fecha="2022-05-07",
                hora="14:43:00",
            ),
            Pedido(
                id_pedido=8,
                id_local=1,
                id_cliente=8,
                fecha="2022-05-07",
                hora="15:41:00",
            ),
        ]

        generador_entregado_asociaciones = (
            asociacion for asociacion in lista_entregada
        )

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_entregado_pedidos, generador_entregado_asociaciones, "2022-05-07"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pizza for pizza in resultado_estudiante]

        lista_esperada = [
            "ERIKA",
            "FURUDO",
            "LOGIC",
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)
