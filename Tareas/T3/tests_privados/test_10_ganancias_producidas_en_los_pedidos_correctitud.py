import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import ganancias_producidas_en_los_pedidos



class TestGananciasProducidasEnLosPedidosCorrectitud(unittest.TestCase):

    def shortDescription(self):

        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que el test funcione si es que que no hay pedidos en el generador
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Setas mágicas_S",
                ingredientes="tomate;queso;champiñones;extra champiñones;extra extrachampiñones",
                precio=7900,
            ),
            Pizza(
                nombre="Vegetariana Suprema_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas;extra champiñones",
                precio=9070,
            ),
            Pizza(
                nombre="Margarita Extra Veggies_M", ingredientes="tomate;queso;albahaca;champiñones", precio=10300
            ),
        ]

        generador_entregado_pizzas = (pizza for pizza in lista_entregada)

        lista_entregada = []

        generador_entregado_contenido_pedidos = (pedido for pedido in lista_entregada)

        resultado_estudiante = ganancias_producidas_en_los_pedidos(
            generador_entregado_contenido_pedidos, generador_entregado_pizzas
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = []

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que el test funcione si es que todos los pedidos tienen un solo producto
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Margarita_S", ingredientes="tomate;queso;albahaca", precio=5000
            ),
            Pizza(
                nombre="Margarita_M", ingredientes="tomate;queso;albahaca", precio=5000
            ),
            Pizza(nombre="Napolitana_L", ingredientes="tomate;queso;jamón", precio=10000),
            Pizza(
                nombre="Locura_S",
                ingredientes="tomate;queso;manjar;pepperoni",
                precio=8000,
            ),
            Pizza(
                nombre="Pepperoni_S", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Olives Máxima_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas; extra aceitunas",
                precio=8050,
            ),
            Pizza(
                nombre="Pollo BBQ_L",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Margarita_M", cantidad=7, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Locura_S", cantidad=20, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Margarita_S", cantidad=10, descuento=0.23
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Pollo BBQ_L", cantidad=3, descuento=0.0
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        resultado_estudiante = ganancias_producidas_en_los_pedidos(
            generador_entregado_contenido_pedidos, generador_entregado_pizzas
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [(1, 35000), (4, 128000), (2, 38500), (5, 30000)]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que el test funcione si es que todos los pedidos tienen más de un producto
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Locura_S",
                ingredientes="tomate;queso;manjar;pepperoni",
                precio=8172,
            ),
            Pizza(
                nombre="Super Espinaca_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas;espinaca;extra espinaca",
                precio=13385,
            ),
            Pizza(
                nombre="Hawaiiana elevada_L",
                ingredientes="piña;super piña;jamón;queso;salsa de tomate",
                precio=11345,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=12945,
            ),
            Pizza(
                nombre="Margarita", ingredientes="tomate;queso;albahaca", precio=5000
            ),
            Pizza(
                nombre="Vegetariana Suprema_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas;extra champiñones",
                precio=9070,
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Locura_S", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(id_pedido=1, nombre="Super Espinaca_M", cantidad=2, descuento=0.0),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana Suprema_M", cantidad=3, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Hawaiiana elevada_L", cantidad=6, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Locura_S", cantidad=7, descuento=0.2
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        resultado_estudiante = ganancias_producidas_en_los_pedidos(
            generador_entregado_contenido_pedidos, generador_entregado_pizzas
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [(1, 43114), (3, 66696), (5, 97543)]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Test que verifique que funcione al haber 5 pedidos de múltiples productos.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica extra spicy_M",
                ingredientes="pepperoni;queso;salsa de tomat;salsa picante",
                precio=8117,
            ),
            Pizza(
                nombre="Pepperoni Clásica extra spicy_S",
                ingredientes="pepperoni;queso;salsa de tomat;salsa picante",
                precio=8010,
            ),
            Pizza(
                nombre="Vegetariana_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=11328,
            ),
            Pizza(
                nombre="Hawaiiana Especial_M",
                ingredientes="piña;jamón;queso;salsa de tomate;manjar",
                precio=12745,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=12342,
            ),
            Pizza(
                nombre="Margarita_S", ingredientes="tomate;queso;albahaca", precio=5000
            ),
            Pizza(
                nombre="Hawaiiana elevada_L",
                ingredientes="piña;super piña;jamón;queso;salsa de tomate",
                precio=11345,
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica extra spicy_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica extra spicy_S", cantidad=2, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Hawaiiana Especial_M", cantidad=4, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.23
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Pepperoni Clásica extra spicy_S", cantidad=6, descuento=0.23
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Pepperoni Clásica extra spicy_M", cantidad=1, descuento=0.1
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Margarita_S", cantidad=2, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Vegetariana_M", cantidad=3, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Hawaiiana elevada_L", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        resultado_estudiante = ganancias_producidas_en_los_pedidos(
            generador_entregado_contenido_pedidos, generador_entregado_pizzas
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            (1, 19310),
            (3, 84964),
            (5, 84523),
            (6, 7305),
            (7, 62555),
            (8, 61710),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Test que verifique que funcione al haber 8 pedidos de múltiples productos.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Supra Pepperoni_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=9000,
            ),
            Pizza(
                nombre="Supra Pepperoni_S",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=8100,
            ),
            Pizza(
                nombre="Vegetariana Máxima_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas dobles",
                precio=11380,
            ),
            Pizza(
                nombre="Vegetariana Máxima_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas dobles",
                precio=10385,
            ),
            Pizza(
                nombre="Hawaiiana_M",
                ingredientes="piña;jamón;queso;salsa de tomate",
                precio=12345,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=12345,
            ),
            Pizza(
                nombre="Margarita_M", ingredientes="tomate;queso;albahaca", precio=5000
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Supra Pepperoni_M", cantidad=3, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=1, nombre="Margarita_M", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana Máxima_M", cantidad=3, descuento=0.15
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Hawaiiana_M", cantidad=3, descuento=0.15
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Supra Pepperoni_M", cantidad=6, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Supra Pepperoni_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Vegetariana Máxima_S", cantidad=2, descuento=0.32
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Margarita_M", cantidad=3, descuento=0.32
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Hawaiiana_M", cantidad=4, descuento=0.32
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Camarones sobre ajo_S", cantidad=51, descuento=0.8
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Supra Pepperoni_S", cantidad=6, descuento=0.8
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Supra Pepperoni_S", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Margarita_M", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Vegetariana Máxima_S", cantidad=4, descuento=0.35
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Hawaiiana_M", cantidad=4, descuento=0.35
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.35
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Supra Pepperoni_S", cantidad=2, descuento=0.35
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        resultado_estudiante = ganancias_producidas_en_los_pedidos(
            generador_entregado_contenido_pedidos, generador_entregado_pizzas
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            (1, 37000),
            (3, 60499),
            (5, 92580),
            (6, 7200),
            (7, 57902),
            (8, 135639),
            (9, 18100),
            (10, 109749),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)
