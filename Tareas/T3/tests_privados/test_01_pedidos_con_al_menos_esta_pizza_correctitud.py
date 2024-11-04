import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from por_copiar.utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import pedidos_con_al_menos_esta_pizza


class TestPedidoConAlMenosEstaPizzaCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que el test funcione si solo hay un pedido de esa pizza en tests pequeños.
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
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_M", cantidad=3, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
        ]

        generador_entregado = (pedido for pedido in lista_entregada)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            generador_entregado, "Camarones sobre ajo"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_M", cantidad=3, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que el test funcione si solo hay tres pedidos de esa pizza en tests pequeños.
        """

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Hawaiiana_M", cantidad=1, descuento=0.22
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Camarones sobre ajo_M", cantidad=4, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Vegetariana_S", cantidad=6, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Vegetariana_M", cantidad=7, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Hawaiiana_M", cantidad=8, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Vegetariana_M", cantidad=7, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Hawaiiana_M", cantidad=10, descuento=0.0
            ),
        ]

        generador_entregado = (pedido for pedido in lista_entregada)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            generador_entregado, "Vegetariana"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
        ContenidoPedido(
            id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.0
        ),
        ContenidoPedido(
            id_pedido=6, nombre="Vegetariana_S", cantidad=6, descuento=0.3
        ),
        ContenidoPedido(
            id_pedido=7, nombre="Vegetariana_M", cantidad=7, descuento=0.0
        ),
        ContenidoPedido(
            id_pedido=9, nombre="Vegetariana_M", cantidad=7, descuento=0.0
        ),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que el test funcione si hay cinco pedidos de esa pizza en tests pequeños.
        """
        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Camarones sobre ajo_S", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Super_M", cantidad=2, descuento=0.22
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Hawaiiana_S", cantidad=6, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Hawaiiana_S", cantidad=7, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Camarones sobre ajo_M", cantidad=8, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Vegetariana_M", cantidad=9, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Hawaiiana_M", cantidad=10, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=11, nombre="Hawaiiana_S", cantidad=11, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=12, nombre="Camarones sobre ajo_S", cantidad=12, descuento=0.0
            ),
        ]

        generador_entregado = (pedido for pedido in lista_entregada)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            generador_entregado, "Hawaiiana"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Hawaiiana_S", cantidad=6, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Hawaiiana_S", cantidad=7, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Hawaiiana_M", cantidad=10, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=11, nombre="Hawaiiana_S", cantidad=11, descuento=0.0
            ),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que el test funcione si hay otra pizza con nombre similar en tests pequeños.
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
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Hawaiiana_S", cantidad=6, descuento=0.3
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
            ContenidoPedido(
                id_pedido=11,
                nombre="HHawaiiana_L",
                cantidad=11,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=12,
                nombre="Hawaiianaaaa_S",
                cantidad=12,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=13,
                nombre="Hawaiiana  hkhiu_S",
                cantidad=13,
                descuento=0.0,
            ),
        ]

        generador_entregado = (pedido for pedido in lista_entregada)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            generador_entregado, "Hawaiiana"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Hawaiiana_S", cantidad=6, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Hawaiiana_M", cantidad=8, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Hawaiiana_M", cantidad=10, descuento=0.0
            ),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que el test funcione si no hay pedidos de esa pizza en tests pequeños.
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
                id_pedido=5, nombre="Margarita_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Hawaiiana_S", cantidad=6, descuento=0.3
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

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            generador_entregado, "Camarones sobre ajo"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_esperada = []

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que el test funcione si todos los pedidos tienen la pizza en tests pequeños.
        """

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Margarita_S", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Margarita_S", cantidad=2, descuento=0.22
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Margarita_M", cantidad=3, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Margarita_S", cantidad=4, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Margarita_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Margarita_L", cantidad=6, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Margarita_S", cantidad=7, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Margarita_S", cantidad=8, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Margarita_M", cantidad=9, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Margarita_S", cantidad=10, descuento=0.0
            ),
        ]

        generador_entregado = (pedido for pedido in lista_entregada)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            generador_entregado, "Margarita"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_esperada = [
            ContenidoPedido(
                id_pedido=1, nombre="Margarita_S", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Margarita_S", cantidad=2, descuento=0.22
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Margarita_M", cantidad=3, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Margarita_S", cantidad=4, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Margarita_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Margarita_L", cantidad=6, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Margarita_S", cantidad=7, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Margarita_S", cantidad=8, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Margarita_M", cantidad=9, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Margarita_S", cantidad=10, descuento=0.0
            ),
        ]

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que el test funcione si se entrega un generador vacío
        """

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = []

        generador_entregado = (pedido for pedido in lista_entregada)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            generador_entregado, "Margarita"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_esperada = []

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        self.assertCountEqual(lista_estudiante, lista_esperada)
