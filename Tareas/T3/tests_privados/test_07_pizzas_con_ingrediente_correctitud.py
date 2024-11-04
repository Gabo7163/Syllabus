import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from tests_privados.solution.test_07 import *
from por_copiar.utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import pizzas_con_ingrediente



class TestPizzasConIngredienteCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que el test funcione si es que el ingrediente no existe en ninguna pizza.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Camarones al ajo", ingredientes="camarones;salsa de tomate;queso", precio=5000
            ),
            Pizza(nombre="Napolitana", ingredientes="tomate;queso;jamón", precio=6000),
            Pizza(
                nombre="Vegetariana Suprema",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas;extra champiñones",
                precio=9000,
            ),
            Pizza(
                nombre="Pepperoni", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Vegetariana",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo BBQ",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = pizzas_con_ingrediente(generador_entregado, "manjar")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = []

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que el test funcione si es que el ingrediente existe en todas las pizzas.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(nombre="Napolitana", ingredientes="tomate;queso;pepperoni", precio=6000),
            Pizza(
                nombre="Hawaiana", ingredientes="tomate;queso;pepperoni;piña", precio=7000
            ),
            Pizza(
                nombre="Pepperoni", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Pollo BBQ",
                ingredientes="tomate;queso;pollo;cebolla;bbq;pepperoni",
                precio=10000,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = pizzas_con_ingrediente(generador_entregado, "pepperoni")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(nombre="Napolitana", ingredientes="tomate;queso;pepperoni", precio=6000),
            Pizza(
                nombre="Hawaiana", ingredientes="tomate;queso;pepperoni;piña", precio=7000
            ),
            Pizza(
                nombre="Pepperoni", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Pollo BBQ",
                ingredientes="tomate;queso;pollo;cebolla;bbq;pepperoni",
                precio=10000,
            ),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que el test funcione si es que el ingrediente existe en tres pizzas.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Margarita Extra Veggies", ingredientes="tomate;queso;albahaca;champiñones", precio=5000
            ),
            Pizza(nombre="Napolitana", ingredientes="tomate;queso;jamón", precio=6000),
            Pizza(
                nombre="Hawaiana", ingredientes="tomate;queso;jamón;piña", precio=7000
            ),
            Pizza(
                nombre="Pepperoni", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Locura",
                ingredientes="tomate;queso;manjar;pepperoni",
                precio=8000,
            ),
            Pizza(
                nombre="Vegetariana Suprema",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas;extra champiñones",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo BBQ",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
            Pizza(
                nombre="supra-pepperoni",
                ingredientes="tomate;queso;pepperoni;pepperoni-doble",
                precio=9050,
            ),
            Pizza(
                nombre="Setas mágicas",
                ingredientes="tomate;queso;champiñones;extra champiñones;extra extrachampiñones",
                precio=9000,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = pizzas_con_ingrediente(generador_entregado, "champiñones")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(
                nombre="Setas mágicas",
                ingredientes="tomate;queso;champiñones;extra champiñones;extra extrachampiñones",
                precio=9000,
            ),
            Pizza(
                nombre="Vegetariana Suprema",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas;extra champiñones",
                precio=9000,
            ),
            Pizza(
                nombre="Margarita Extra Veggies", ingredientes="tomate;queso;albahaca;champiñones", precio=5000
            ),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que el test funcione si es que el ingrediente existe en una pizza.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Margarita", ingredientes="tomate;queso;albahaca", precio=5000
            ),
            Pizza(nombre="Napolitana", ingredientes="tomate;queso;jamón", precio=6000),
            Pizza(
                nombre="Locura",
                ingredientes="tomate;queso;manjar;pepperoni",
                precio=8000,
            ),
            Pizza(
                nombre="Pepperoni", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Olives Máxima",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas; extra aceitunas",
                precio=8050,
            ),
            Pizza(
                nombre="Pollo BBQ",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = pizzas_con_ingrediente(generador_entregado, "aceitunas")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(
                nombre="Olives Máxima",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas; extra aceitunas",
                precio=8050,
            ),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que el test funcione si es que el generador entregado está vacío.
        """

        lista_entregada = []

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = pizzas_con_ingrediente(generador_entregado, "salsa de tomate")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = []

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que el test funcione si es que el generador entregado tiene solo una pizza.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Locura",
                ingredientes="tomate;queso;manjar;pepperoni",
                precio=8000,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = pizzas_con_ingrediente(generador_entregado, "manjar")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(
                nombre="Locura",
                ingredientes="tomate;queso;manjar;pepperoni",
                precio=8000,
            ),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que el test funcione si es que el existen ingredientes con nombre parecido.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Margarita manjarate special", ingredientes="tomate;manjare;albahaca", precio=5000
            ),
            Pizza(
                nombre="Napolitana manjarate special", ingredientes="salsa de manjar;queso;jamón", precio=6000
            ),
            Pizza(
                nombre="Vegetariana manjarate special",
                ingredientes="tomate;queso;manjar;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Hawaiana manjarate special", ingredientes="tomate;queso;manjar a la crema;piña", precio=7000
            ),
            Pizza(
                nombre="Pepperoni manjarate special", ingredientes="salsa de tomate;mmmanjar;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Pollo BBQ manjarate special",
                ingredientes="tomate;queso;pollo;cebolla;manjar",
                precio=10000,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = pizzas_con_ingrediente(generador_entregado, "manjar")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(
                nombre="Vegetariana manjarate special",
                ingredientes="tomate;queso;manjar;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo BBQ manjarate special",
                ingredientes="tomate;queso;pollo;cebolla;manjar",
                precio=10000,
            ),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada) 

