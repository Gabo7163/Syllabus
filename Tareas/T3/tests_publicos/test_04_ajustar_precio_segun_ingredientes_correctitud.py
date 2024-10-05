import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from utilidades import N_SECOND

from consultas import ajustar_precio_segun_ingredientes


class TestAjustarPrecioSegunIngredientesCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica funcionamiento correcto cuando no hay pizzas con el ingrediente determinado.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(nombre="Marge_S", ingredientes="tomate;queso;albahaca", precio=8000),
            Pizza(nombre="Napolitan_S", ingredientes="tomate;queso;jamón", precio=7600),
            Pizza(
                nombre="Hawaiana_S", ingredientes="tomate;queso;jamón;piña", precio=7000
            ),
            Pizza(
                nombre="Pepperoni_S", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo BBQ_S",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_entregado, "pepinillos", 1000
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = []

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica funcionamiento correcto cuando solamente se modifica el precio de una pizza.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(nombre="Marga_S", ingredientes="tomate;queso;albahaca", precio=8000),
            Pizza(nombre="Napolitan_S", ingredientes="tomate;queso;jamón", precio=7600),
            Pizza(
                nombre="Hawaiana_XL",
                ingredientes="tomate;queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="Pepperoni_S", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo BBQ_S",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_entregado, "aceitunas", 50
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9050,
            )
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica funcionamiento correcto cuando se modifica el precio de dos o más pizzas.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(nombre="Marga_S", ingredientes="tomate;queso;albahaca", precio=9000),
            Pizza(nombre="Napolitan_S", ingredientes="tomate;queso;jamón", precio=7900),
            Pizza(
                nombre="Hawaiana_S",
                ingredientes="tomate;queso;jamón;piña",
                precio=17000,
            ),
            Pizza(
                nombre="Pepperoni_S", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=99000,
            ),
            Pizza(
                nombre="Pollo BBQ_S",
                ingredientes="queso;pollo;cebolla;bbq",
                precio=10000,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_entregado, "tomate", 1200
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(nombre="Marga_S", ingredientes="tomate;queso;albahaca", precio=10200),
            Pizza(nombre="Napolitan_S", ingredientes="tomate;queso;jamón", precio=9100),
            Pizza(
                nombre="Hawaiana_S",
                ingredientes="tomate;queso;jamón;piña",
                precio=18200,
            ),
            Pizza(
                nombre="Pepperoni_S", ingredientes="tomate;queso;pepperoni", precio=9200
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=100200,
            ),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica funcionamiento correcto cuando la diferencia de precio sea 0.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(nombre="Marga_S", ingredientes="tomate;queso;albahaca", precio=98000),
            Pizza(
                nombre="Naplitan_S", ingredientes="tomate;queso;jamón", precio=7000600
            ),
            Pizza(nombre="Hawaana_S", ingredientes="tomate;jamón;piña", precio=7000),
            Pizza(nombre="Peroni_S", ingredientes="queso;pepperoni", precio=8000),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo BBQ_L",
                ingredientes="tomate;pollo;cebolla;bbq",
                precio=10000,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_entregado, "queso", 0
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(nombre="Peroni_S", ingredientes="queso;pepperoni", precio=8000),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(nombre="Marga_S", ingredientes="tomate;queso;albahaca", precio=98000),
            Pizza(
                nombre="Naplitan_S", ingredientes="tomate;queso;jamón", precio=7000600
            ),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica funcionamiento correcto cuando la diferencia de precio sea negativa.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Marga_XL", ingredientes="tomate;queso;albahaca", precio=98000
            ),
            Pizza(nombre="Naplitan_S", ingredientes="tomate;queso;jamón", precio=70543),
            Pizza(nombre="Hawaana_S", ingredientes="tomate;jamón;piña", precio=7000),
            Pizza(nombre="Perfoni_S", ingredientes="queso;pepperoni", precio=80004),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=90400,
            ),
            Pizza(
                nombre="Pollo BBQ_S",
                ingredientes="tomate;pollo;cebolla;bbq",
                precio=8900,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_entregado, "queso", -8000
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(nombre="Perfoni_S", ingredientes="queso;pepperoni", precio=72004),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=82400,
            ),
            Pizza(
                nombre="Marga_XL", ingredientes="tomate;queso;albahaca", precio=90000
            ),
            Pizza(nombre="Naplitan_S", ingredientes="tomate;queso;jamón", precio=62543),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica funcionamiento correcto cuando la diferencia de precio deje el valor de la pizza en 7000 (pues es la cota inferior).
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Marga_S", ingredientes="tomate;queso;albahaca;kd", precio=9424
            ),
            Pizza(
                nombre="Naplitan 2E INFINITO PODER_S",
                ingredientes="tomate;queso;jamón;kd",
                precio=70543,
            ),
            Pizza(nombre="Hawaana_S", ingredientes="tomate;jamón;piña;kd", precio=7000),
            Pizza(nombre="Perfoni_S", ingredientes="queso;pepperoni;kd", precio=80004),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas;kd",
                precio=90534532,
            ),
            Pizza(
                nombre="Pollo BBQ_S",
                ingredientes="tomate;pollo;cebolla;bbq",
                precio=8900,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_entregado, "kd", -80000
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(nombre="Perfoni_S", ingredientes="queso;pepperoni;kd", precio=7000),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas;kd",
                precio=90454532,
            ),
            Pizza(
                nombre="Marga_S", ingredientes="tomate;queso;albahaca;kd", precio=7000
            ),
            Pizza(
                nombre="Naplitan 2E INFINITO PODER_S",
                ingredientes="tomate;queso;jamón;kd",
                precio=7000,
            ),
            Pizza(nombre="Hawaana_S", ingredientes="tomate;jamón;piña;kd", precio=7000),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica funcionamiento correcto cuando se tienen ingredientes que son substrings de otros ingredientes.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="DROP TABLE Marga_S",
                ingredientes="substring;queso;albahaca;kd",
                precio=9424,
            ),
            Pizza(
                nombre="Naplitan 2E INFINITO PODER_XL",
                ingredientes="substri;tomate;substrin;salsa de substring;substring a lo BBQ;queso;jamón;substr",
                precio=70543,
            ),
            Pizza(nombre="Hawaana_S", ingredientes="tomate;jamón;piña;kd", precio=7000),
            Pizza(
                nombre="THE REAL Perfoni_L",
                ingredientes="queso;pepperoni;substring",
                precio=80004,
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;substrin;salsa de substring;pimentón;aceitunas;kd",
                precio=90534532,
            ),
            Pizza(
                nombre="Pollo BBQ_XL",
                ingredientes="tomate;substri;pollo;sub;cebolla;bbq;substrin",
                precio=8900,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_entregado, "substring", -30
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(
                nombre="DROP TABLE Marga_S",
                ingredientes="substring;queso;albahaca;kd",
                precio=9394,
            ),
            Pizza(
                nombre="THE REAL Perfoni_L",
                ingredientes="queso;pepperoni;substring",
                precio=79974,
            ),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)
