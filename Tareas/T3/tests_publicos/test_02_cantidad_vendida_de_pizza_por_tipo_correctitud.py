import os
import sys
import unittest
from collections import namedtuple

from tests_publicos.timeout_function import timeout
from utilidades import N_SECOND

from consultas import cantidad_vendida_de_pizza_por_tipo



class TestCantidadVendidaDePizzaPorTipoCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica funcionamiento correcto cuando no existe en los pedidos pizza del tipo.
        """

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1,
                nombre="Pepperoni Ultra Clásica_M",
                cantidad=1,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=2,
                nombre="Pepperoni Mega Clásica_M",
                cantidad=43,
                descuento=0.22,
            ),
            ContenidoPedido(id_pedido=3, nombre="Vegana_S", cantidad=3, descuento=0.0),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones con ajo_M", cantidad=1, descuento=0.5
            ),
        ]

        generador_entregado = (pedido for pedido in lista_entregada)

        int_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_entregado, "Pepperoni Clásica"
        )

        self.assertIsInstance(int_estudiante, (int))

        int_esperado = 0

        self.assertEqual(int_estudiante, int_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica funcionamiento correcto cuando existe solamente una pizza vendida del tipo, en solo un tamaño.
        """

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1,
                nombre="Pepperoni Ultra Ultra Clásica_M",
                cantidad=1000,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=2,
                nombre="Pepperoni Clásica_S",
                cantidad=1,
                descuento=0.22,
            ),
            ContenidoPedido(id_pedido=3, nombre="Vegana_S", cantidad=3, descuento=0.0),
            ContenidoPedido(
                id_pedido=40, nombre="Hawaiiana_M", cantidad=4, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones CONCAT ajo_XL", cantidad=1, descuento=0.5
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Pepperoni Clásicas_M", cantidad=1, descuento=0.3
            ),
        ]

        generador_entregado = (pedido for pedido in lista_entregada)

        int_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_entregado, "Pepperoni Clásica"
        )
        self.assertIsInstance(int_estudiante, (int))

        int_esperado = 1

        self.assertEqual(int_estudiante, int_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica funcionamiento correcto cuando existe más de una pizza vendida del tipo, en solo un tamaño.
        """

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1,
                nombre="Pepperoni Clásica Genial_S",
                cantidad=20,
                descuento=0.1,
            ),
            ContenidoPedido(
                id_pedido=2,
                nombre="Peppe Clásica_M",
                cantidad=2,
                descuento=0.22,
            ),
            ContenidoPedido(id_pedido=3, nombre="Vegana_S", cantidad=3, descuento=0.0),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaii Ana_M", cantidad=6, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5,
                nombre="Camarones MEGA CONCAT ULTRA ajo_M",
                cantidad=1,
                descuento=0.5,
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Hawaii Ana_M", cantidad=2, descuento=0.0
            ),
        ]

        generador_entregado = (pedido for pedido in lista_entregada)

        int_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_entregado, "Hawaii Ana"
        )

        self.assertIsInstance(int_estudiante, (int))

        int_esperado = 8

        self.assertEqual(int_estudiante, int_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica funcionamiento correcto cuando existe más de una pizza vendida del tipo, en más de un tamaño.
        """

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1,
                nombre="Pepperoni Falsa_S",
                cantidad=3,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=2,
                nombre="Pepperoni Mega Clásica_M",
                cantidad=5000,
                descuento=0.22,
            ),
            ContenidoPedido(id_pedido=3, nombre="Vegana_S", cantidad=3, descuento=0.0),
            ContenidoPedido(
                id_pedido=4, nombre="Pepperoni Falsa_M", cantidad=2412, descuento=0.0
            ),
            ContenidoPedido(id_pedido=5, nombre="Hawana_XL", cantidad=2, descuento=0.0),
            ContenidoPedido(
                id_pedido=6, nombre="CONCAT PANDAS ajo_M", cantidad=2, descuento=0.5
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Pepperoni Falsa_XL", cantidad=5, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=8,
                nombre="Pepperoni Mega Mega Clásica_M",
                cantidad=54,
                descuento=0.21,
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Pepperoni Falsa_XL", cantidad=23, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Pepperoni L IS REAL_L", cantidad=3, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=11, nombre="Vegana_S", cantidad=1000, descuento=0.0
            ),
        ]

        generador_entregado = (pedido for pedido in lista_entregada)

        int_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_entregado, "Pepperoni Falsa"
        )

        self.assertIsInstance(int_estudiante, (int))

        int_esperado = 2443

        self.assertEqual(int_estudiante, int_esperado)
