import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

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
            Pizza(
                nombre="Marge_S",
                ingredientes="tomate;fallout;queso;albahaca",
                precio=8000,
            ),
            Pizza(
                nombre="Napolitan_S",
                ingredientes="tomate;queso;jamón;el;deseo",
                precio=7630,
            ),
            Pizza(
                nombre="Hawaiana_S",
                ingredientes="tomate;bbq1X;queso;jamón;piña",
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
            generador_entregado, "bbq12", 23465
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
            generador_entregado, "bbq", 4352
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(
                nombre="Pollo BBQ_S",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=14352,
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
                nombre="Pepperoni_S",
                ingredientes="pepperoni;salsa de queso",
                precio=8000,
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=99000,
            ),
            Pizza(
                nombre="Pollo BBQ_S",
                ingredientes="pollo;cebolla;bbq",
                precio=10000,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_entregado, "queso", 2000
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(nombre="Marga_S", ingredientes="tomate;queso;albahaca", precio=11000),
            Pizza(nombre="Napolitan_S", ingredientes="tomate;queso;jamón", precio=9900),
            Pizza(
                nombre="Hawaiana_S",
                ingredientes="tomate;queso;jamón;piña",
                precio=19000,
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=101000,
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
            Pizza(
                nombre="Marga_S", ingredientes="tomate;queso;albahaca;ou", precio=9532
            ),
            Pizza(
                nombre="Naplitan_S", ingredientes="tomate;queso;jamón", precio=700032432
            ),
            Pizza(nombre="Hawaana_S", ingredientes="tomate;ou;jamón;piña", precio=7432),
            Pizza(nombre="Peroni_S", ingredientes="queso;pepperoni", precio=8000),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo MEGA MEGA MEGA BBQ_L",
                ingredientes="tomate;pollo;cebolla;bbq",
                precio=10000,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_entregado, "ou", 0
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(
                nombre="Marga_S", ingredientes="tomate;queso;albahaca;ou", precio=9532
            ),
            Pizza(nombre="Hawaana_S", ingredientes="tomate;ou;jamón;piña", precio=7432),
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
                nombre="Marga_XL",
                ingredientes="tomate;queso;albahaca;aceituna",
                precio=98000,
            ),
            Pizza(nombre="Naplitan_S", ingredientes="tomate;queso;jamón", precio=70543),
            Pizza(nombre="Hawaana_S", ingredientes="tomate;jamón;piña", precio=7000),
            Pizza(
                nombre="FAKE OR TRUTH Perfoni_S",
                ingredientes="queso;pepperoni",
                precio=80004,
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=90400,
            ),
            Pizza(
                nombre="Pollo BBQ_S",
                ingredientes="manjar;tomate;pollo;cebolla;bbq",
                precio=8900,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_entregado, "pepperoni", -5002
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(
                nombre="FAKE OR TRUTH Perfoni_S",
                ingredientes="queso;pepperoni",
                precio=75002,
            ),
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
                ingredientes="tomate;queso;jamón;EL besto;kd",
                precio=8932,
            ),
            Pizza(
                nombre="Hawaana_S",
                ingredientes="tomate;jamón;piña;besto;kd",
                precio=7000,
            ),
            Pizza(
                nombre="Perfoni_S", ingredientes="queso;el;pepperoni;kd", precio=80004
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;EL besto;queso;champiñones;pimentón;aceitunas;kd",
                precio=90534532,
            ),
            Pizza(
                nombre="Pollo QQ BBQ_S",
                ingredientes="EL besto;tomate;pollo;cebolla;bbq",
                precio=8900,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_entregado, "EL besto", -74352
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(
                nombre="Naplitan 2E INFINITO PODER_S",
                ingredientes="tomate;queso;jamón;EL besto;kd",
                precio=7000,
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;EL besto;queso;champiñones;pimentón;aceitunas;kd",
                precio=90460180,
            ),
            Pizza(
                nombre="Pollo QQ BBQ_S",
                ingredientes="EL besto;tomate;pollo;cebolla;bbq",
                precio=7000,
            ),
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
                ingredientes="substring;queso;albahaca;kd;substrin 2.0.1.14",
                precio=9424,
            ),
            Pizza(
                nombre="Naplitan 2E INFINITO PODER_XL",
                ingredientes="substri;tomate;substrin;salsa de substring;substring a lo BBQ;queso;jamón;substr",
                precio=70543,
            ),
            Pizza(
                nombre="Hawaana_S",
                ingredientes="sub;tomate;jamón;piña;substring EL REGRESO",
                precio=7000,
            ),
            Pizza(
                nombre="THE REAL Perfoni_L",
                ingredientes="substri;queso;pepperoni;substring",
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
            generador_entregado, "substrin", -1
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(
                nombre="Naplitan 2E INFINITO PODER_XL",
                ingredientes="substri;tomate;substrin;salsa de substring;substring a lo BBQ;queso;jamón;substr",
                precio=70542,
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;substrin;salsa de substring;pimentón;aceitunas;kd",
                precio=90534531,
            ),
            Pizza(
                nombre="Pollo BBQ_XL",
                ingredientes="tomate;substri;pollo;sub;cebolla;bbq;substrin",
                precio=8899,
            ),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)
