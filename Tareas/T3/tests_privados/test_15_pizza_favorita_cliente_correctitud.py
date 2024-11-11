import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from tests_privados.solution.test_15 import *
from utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

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
                id_pedido=1,
                id_local=1,
                id_cliente=1,
                fecha="2021-01-29",
                hora="12:00:00",
            ),
            Pedido(
                id_pedido=2,
                id_local=1,
                id_cliente=1,
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
                fecha="2010-01-01",
                hora="12:00:00",
            ),
            Pedido(
                id_pedido=6,
                id_local=1,
                id_cliente=11,
                fecha="2021-01-01",
                hora="13:00:00",
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
                nombre="Pepperoni N Automata Clásica_M",
                cantidad=4,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=2,
                nombre="Pepperoni I Automata Clásica_XL",
                cantidad=10,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=3,
                nombre="Vegetariana E KNOX Normal_M",
                cantidad=6,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=4, nombre="The RND is Near_M", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5,
                nombre="CONcat DECALOGU E ajo_S",
                cantidad=30,
                descuento=0.0,
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        resultado_estudiante = pizza_favorita_cliente(
            generador_entregado_asociaciones, generador_entregado_pedidos, 10
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
                id_cliente=3,
                fecha="2022-02-03",
                hora="18:30:00",
            ),
            Pedido(
                id_pedido=5,
                id_local=1,
                id_cliente=3,
                fecha="2010-01-01",
                hora="12:00:00",
            ),
            Pedido(
                id_pedido=6,
                id_local=1,
                id_cliente=6,
                fecha="2021-01-01",
                hora="13:00:00",
            ),
            Pedido(
                id_pedido=7,
                id_local=1,
                id_cliente=4,
                fecha="2023-05-05",
                hora="12:30:00",
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
                id_pedido=3, nombre="Vegetariana Normal_M", cantidad=29, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepe de Hawaiiana_M", cantidad=15, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Pepe de Hawaiiana_M", cantidad=15, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Pepperoni Clásica_M", cantidad=24, descuento=0.0
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        resultado_estudiante = pizza_favorita_cliente(
            generador_entregado_asociaciones, generador_entregado_pedidos, 3
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [tupla for tupla in resultado_estudiante]

        lista_esperada = [("Pepe de Hawaiiana", 30)]

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
                id_pedido=1,
                id_local=1,
                id_cliente=7,
                fecha="2021-01-29",
                hora="12:00:00",
            ),
            Pedido(
                id_pedido=2,
                id_local=7,
                id_cliente=1,
                fecha="2021-04-05",
                hora="12:30:00",
            ),
            Pedido(
                id_pedido=3,
                id_local=1,
                id_cliente=7,
                fecha="2021-05-07",
                hora="17:00:00",
            ),
            Pedido(
                id_pedido=4,
                id_local=1,
                id_cliente=7,
                fecha="2022-02-03",
                hora="18:30:00",
            ),
            Pedido(
                id_pedido=5,
                id_local=1,
                id_cliente=7,
                fecha="2010-01-01",
                hora="12:00:00",
            ),
            Pedido(
                id_pedido=6,
                id_local=1,
                id_cliente=6,
                fecha="2021-01-01",
                hora="13:00:00",
            ),
            Pedido(
                id_pedido=7,
                id_local=1,
                id_cliente=7,
                fecha="2023-05-05",
                hora="12:30:00",
            ),
            Pedido(
                id_pedido=8,
                id_local=1,
                id_cliente=7,
                fecha="2023-08-05",
                hora="12:35:00",
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
                nombre="Pepperoni FAKE Clásica_S",
                cantidad=12,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana Normal_M", cantidad=26, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4,
                nombre="Pepe FAKE  ZX DIALOGUE OPTIONAL_M",
                cantidad=90,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=5,
                nombre="Camarones BONOS BONUS bajo ajo_S",
                cantidad=83,
                descuento=0.3,
            ),
            ContenidoPedido(
                id_pedido=7,
                nombre="Pepperoni FAKE Clásica_L",
                cantidad=50,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=8,
                nombre="Pepperoni FAKE Clásica_XL",
                cantidad=51,
                descuento=0.0,
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        resultado_estudiante = pizza_favorita_cliente(
            generador_entregado_asociaciones, generador_entregado_pedidos, 7
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [tupla for tupla in resultado_estudiante]

        lista_esperada = [("Pepperoni FAKE Clásica", 101)]

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
                id_pedido=1,
                id_local=1,
                id_cliente=4,
                fecha="2021-01-29",
                hora="12:00:00",
            ),
            Pedido(
                id_pedido=2,
                id_local=1,
                id_cliente=4,
                fecha="2021-04-05",
                hora="12:30:00",
            ),
            Pedido(
                id_pedido=3,
                id_local=1,
                id_cliente=4,
                fecha="2021-05-07",
                hora="17:00:00",
            ),
            Pedido(
                id_pedido=4,
                id_local=1,
                id_cliente=2,
                fecha="2022-02-03",
                hora="18:30:00",
            ),
            Pedido(
                id_pedido=5,
                id_local=1,
                id_cliente=4,
                fecha="2010-01-01",
                hora="12:00:00",
            ),
            Pedido(
                id_pedido=6,
                id_local=1,
                id_cliente=6,
                fecha="2021-01-01",
                hora="13:00:00",
            ),
            Pedido(
                id_pedido=7,
                id_local=1,
                id_cliente=4,
                fecha="2023-05-05",
                hora="12:30:00",
            ),
            Pedido(
                id_pedido=8,
                id_local=1,
                id_cliente=4,
                fecha="2023-08-05",
                hora="12:35:00",
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
                id_pedido=3, nombre="TATSU_M", cantidad=7002, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepe de Hawaiiana_M", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="MAKI_XL", cantidad=7002, descuento=0.0
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

        lista_esperada = [("TATSU", 7002), ("MAKI", 7002)]

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
                id_pedido=1,
                id_local=1,
                id_cliente=90,
                fecha="2021-01-29",
                hora="12:42:00",
            ),
            Pedido(
                id_pedido=2,
                id_local=1,
                id_cliente=90,
                fecha="2021-04-05",
                hora="12:30:00",
            ),
            Pedido(
                id_pedido=3,
                id_local=1,
                id_cliente=90,
                fecha="2021-05-07",
                hora="17:00:00",
            ),
            Pedido(
                id_pedido=4,
                id_local=1,
                id_cliente=2,
                fecha="2022-02-03",
                hora="18:30:00",
            ),
            Pedido(
                id_pedido=5,
                id_local=1,
                id_cliente=90,
                fecha="2010-01-01",
                hora="12:00:00",
            ),
            Pedido(
                id_pedido=6,
                id_local=1,
                id_cliente=6,
                fecha="2021-01-02",
                hora="13:42:00",
            ),
            Pedido(
                id_pedido=7,
                id_local=1,
                id_cliente=90,
                fecha="2023-05-05",
                hora="12:30:00",
            ),
            Pedido(
                id_pedido=8,
                id_local=1,
                id_cliente=4,
                fecha="2023-08-05",
                hora="12:35:00",
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
                nombre="This is not_XL",
                cantidad=8990,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=2,
                nombre="This is not_S",
                cantidad=20,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=3,
                nombre="Vege Gaussian Normal_M",
                cantidad=9010,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=6,
                nombre="Pepe de Hawaiiana_M",
                cantidad=252352342,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=5, nombre="F AKECHI_M", cantidad=9010, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=7,
                nombre="Pepperoni Mega Clásica_M",
                cantidad=9008,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=8,
                nombre="Pepperoni EL DESTINO_S",
                cantidad=99999999,
                descuento=0.0,
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        resultado_estudiante = pizza_favorita_cliente(
            generador_entregado_asociaciones, generador_entregado_pedidos, 90
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [tupla for tupla in resultado_estudiante]

        lista_esperada = [
            ("F AKECHI", 9010),
            ("This is not", 9010),
            ("Vege Gaussian Normal", 9010),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)
