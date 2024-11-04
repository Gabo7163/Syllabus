import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from tests_privados.solution.test_03 import *
from por_copiar.utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import pedido_con_mayor_descuento_utilizado



class TestPedidoConMayorDescuentoUtilizadoCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que el test funcione si es que no hay pedidos con descuentos
        """

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Camarones sobre ajo_L", cantidad=3, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Napolitana_M", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Margarita_M", cantidad=4, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_M", cantidad=5, descuento=0.0
            ),
        ]

        generador_entregado = (pedido for pedido in lista_entregada)

        resultado_estudiante = pedido_con_mayor_descuento_utilizado(generador_entregado)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado_estudiante = list(resultado_estudiante)

        resultado_esperado = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Camarones sobre ajo_L", cantidad=3, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Napolitana_M", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Margarita_M", cantidad=4, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_M", cantidad=5, descuento=0.0
            ),
        ]

        self.assertTrue(
            all(elem in resultado_estudiante for elem in resultado_esperado)
        )

        largo_estudiante = len(resultado_estudiante)

        largo_esperado = len(resultado_esperado)

        self.assertEqual(largo_estudiante, largo_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que el test funcione si hay dos descuentos empatados.
        """

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.22
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Margarita_S", cantidad=5, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Hawaiiana_S", cantidad=6, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Vegetariana_M", cantidad=7, descuento=0
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Hawaiiana_M", cantidad=8, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Napolitana_M", cantidad=9, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Hawaiiana_M", cantidad=10, descuento=0.0
            ),
        ]

        generador_entregado = (pedido for pedido in lista_entregada)

        resultado_estudiante = pedido_con_mayor_descuento_utilizado(generador_entregado)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado_estudiante = list(resultado_estudiante)

        resultado_esperado = [
            ContenidoPedido(
                id_pedido=6, nombre="Hawaiiana_S", cantidad=6, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Napolitana_M", cantidad=9, descuento=0.4
            ),
        ]

        self.assertTrue(
            all(elem in resultado_estudiante for elem in resultado_esperado)
        )

        largo_estudiante = len(resultado_estudiante)

        largo_esperado = len(resultado_esperado)

        self.assertEqual(largo_estudiante, largo_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que el test funcione si hay tres descuentos empatados.
        """
        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Camarones sobre ajo_S", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.22
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Napolitana_S", cantidad=5, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Hawaiiana_S", cantidad=6, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Camarones sobre ajo_S", cantidad=7, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Hawaiiana_M", cantidad=8, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Vegetariana_M", cantidad=9, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Margarita_M", cantidad=10, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=11, nombre="Camarones sobre ajo_S", cantidad=11, descuento=0.59
            ),
            ContenidoPedido(
                id_pedido=12, nombre="Camarones sobre ajo_S", cantidad=12, descuento=0.0
            ),
        ]

        generador_entregado = (pedido for pedido in lista_entregada)

        resultado_estudiante = pedido_con_mayor_descuento_utilizado(generador_entregado)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado_estudiante = list(resultado_estudiante)

        resultado_esperado = [
            ContenidoPedido(
                id_pedido=10, nombre="Margarita_M", cantidad=10, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Napolitana_S", cantidad=5, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Margarita_M", cantidad=10, descuento=0.6
            ),
        ]

        self.assertTrue(
            all(elem in resultado_estudiante for elem in resultado_esperado)
        )

        largo_estudiante = len(resultado_estudiante)

        largo_esperado = len(resultado_esperado)

        self.assertEqual(largo_estudiante, largo_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que el test funcione en un caso en el que hay un descuento mayor que el resto.
        """
        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.8
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Hawaiiana_S", cantidad=6, descuento=0.79
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Vegetariana_M", cantidad=7, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Hawaiiana_M", cantidad=8, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Vegetariana_M", cantidad=9, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Hawaiiana_M", cantidad=10, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=11,
                nombre="Camarones sobre ajou_SL",
                cantidad=11,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=12,
                nombre="Camarones sobre ajjjo_S",
                cantidad=12,
                descuento=0.1,
            ),
            ContenidoPedido(
                id_pedido=13,
                nombre="Camarones sobrei ajo_S",
                cantidad=13,
                descuento=0.0,
            ),
        ]

        generador_entregado = (pedido for pedido in lista_entregada)

        resultado_estudiante = pedido_con_mayor_descuento_utilizado(generador_entregado)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado_estudiante = list(resultado_estudiante)

        resultado_esperado = [
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.8
            )
        ]

        self.assertTrue(
            all(elem in resultado_estudiante for elem in resultado_esperado)
        )

        largo_estudiante = len(resultado_estudiante)

        largo_esperado = len(resultado_esperado)

        self.assertEqual(largo_estudiante, largo_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que el test funcione si hay un único descuento
        """

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Napolitana_M", cantidad=2, descuento=0.7
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
            ContenidoPedido(
                id_pedido=6, nombre="Hawaiiana_S", cantidad=6, descuento=0
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Vegetariana_M", cantidad=7, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Hawaiiana_M", cantidad=8, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Vegetariana_M", cantidad=9, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Hawaiiana_M", cantidad=10, descuento=0.0
            ),
        ]

        generador_entregado = (pedido for pedido in lista_entregada)

        resultado_estudiante = pedido_con_mayor_descuento_utilizado(generador_entregado)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado_estudiante = list(resultado_estudiante)

        resultado_esperado = [
            ContenidoPedido(
                id_pedido=2, nombre="Napolitana_M", cantidad=2, descuento=0.7
            )
        ]

        self.assertTrue(
            all(elem in resultado_estudiante for elem in resultado_esperado)
        )

        largo_estudiante = len(resultado_estudiante)

        largo_esperado = len(resultado_esperado)

        self.assertEqual(largo_estudiante, largo_esperado)
