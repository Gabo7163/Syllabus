import os
import sys
import unittest
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from tests_privados.solution.test_anidados import *
from por_copiar.utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import consulta_anidada




class TestConsultaAnidada(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que el test funcione para una consulta simple sobre las pizzas con piña.
        """

        path_pizzas = os.path.join("data_tests_privados", "s", "pizzas.csv")

        consulta = {
            "funcion": "pizzas_con_ingrediente",
            "generador_pizzas": {"funcion": "cargar_pizzas", "path": path_pizzas},
            "ingrediente": "tocino",
        }

        consulta_0 = consulta_anidada(consulta)

        self.assertIsInstance(consulta_0, Iterable)

        resultado_esperado = RESULTADO_CONSULTA_ANIDADA_0

        self.assertCountEqual(list(consulta_0), resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que el test funcione para una consulta acerca de todas las pizzas pagables
        con 9200 de tamaño S con tomate.
        """

        path_pizzas = os.path.join("data_tests_privados", "s", "pizzas.csv")

        consulta = {
            "funcion": "pizzas_pagables_de_un_tamano",
            "generador_pizzas": {
                "funcion": "pizzas_con_ingrediente",
                "generador_pizzas": {"funcion": "cargar_pizzas", "path": path_pizzas},
                "ingrediente": "salsa de tomate",
            },
            "dinero": 9200,
            "tamano": "S",
        }

        consulta_1 = consulta_anidada(consulta)

        self.assertIsInstance(consulta_1, Iterable)

        resultado_esperado = RESULTADO_CONSULTA_ANIDADA_1

        self.assertCountEqual(list(consulta_1), resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que el test funcione para una consulta acerca del total ahorrado para
        pizzas pagables con 10000 de tamaño S con tomate.
        """

        path_pizzas = os.path.join("data_tests_privados", "s", "pizzas.csv")

        path_contenido_pedidos = os.path.join(
            "data_tests_privados", "s", "contenido_pedidos.csv")

        consulta = {
            "funcion": "total_ahorrado_pedidos",
            "generador_contenido_pedidos": {
                "funcion": "cargar_contenido_pedidos",
                "path": path_contenido_pedidos,
            },
            "generador_pizzas": {
                "funcion": "pizzas_pagables_de_un_tamano",
                "generador_pizzas": {
                    "funcion": "pizzas_con_ingrediente",
                    "generador_pizzas": {
                        "funcion": "cargar_pizzas",
                        "path": path_pizzas,
                    },
                    "ingrediente": "palta",
                },
                "dinero": 10200,
                "tamano": "S",
            },
        }

        consulta_2 = consulta_anidada(consulta)

        self.assertIsInstance(consulta_2, int)

        resultado_esperado = RESULTADO_CONSULTA_ANIDADA_2

        self.assertEqual(consulta_2, resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que el test funcione para una consulta acerca pizzas las cuales un cliente
        que no le gusta el tomate puede comer.
        """
        path_pizzas = os.path.join("data_tests_privados", "s", "pizzas.csv")

        consulta = {
            "funcion": "cliente_indeciso",
            "generador_pizzas": {"funcion": "cargar_pizzas", "path": path_pizzas},
            "ingrediente_no_deseado": "salsa de tomate",
            "cantidad_pizzas": 9,
        }

        consulta_3 = consulta_anidada(consulta)

        self.assertIsInstance(consulta_3, Iterable)

        resultado_esperado = RESULTADO_CONSULTA_ANIDADA_3

        self.assertCountEqual(list(consulta_3), resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que el test funcione para una consulta acerca de lo que se puede ahorrar
        un cliente que quiere 9 pizzas y no le gusta la salsa de tomate
        """
        path_pizzas = os.path.join("data_tests_privados", "s", "pizzas.csv")

        path_contenido_pedidos = os.path.join("data_tests_privados", "s", "contenido_pedidos.csv")

        consulta = {
            "funcion": "total_ahorrado_pedidos",
            "generador_pizzas": {
                "funcion": "cliente_indeciso",
                "generador_pizzas": {"funcion": "cargar_pizzas", "path": path_pizzas},
                "ingrediente_no_deseado": "tomate",
                "cantidad_pizzas": 9,
            },
            "generador_contenido_pedidos": {
                "funcion": "cargar_contenido_pedidos",
                "path": path_contenido_pedidos,
            },
        }

        consulta_4 = consulta_anidada(consulta)

        self.assertIsInstance(consulta_4, int)

        resultado_esperado = RESULTADO_CONSULTA_ANIDADA_4

        self.assertEqual(consulta_4, resultado_esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que el test funcione para una consulta acerca de la cantidad de empleados
        en Chile.
        """
        path_locales = os.path.join("data_tests_privados", "l", "locales.csv")

        consulta = {
            "funcion": "cantidad_empleados_pais",
            "generador_locales": {"funcion": "cargar_locales", "path": path_locales},
            "pais": "Chile",
        }

        consulta_5 = consulta_anidada(consulta)

        self.assertIsInstance(consulta_5, int)

        resultado_esperado = RESULTADO_CONSULTA_ANIDADA_5

        self.assertEqual(consulta_5, resultado_esperado)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que el test funcione para una consulta acerca de comprar 
        una pizza con el total ahorrado en otro pedidos.
        """

        path_pizzas = os.path.join("data_tests_privados", "m", "pizzas.csv")
        path_contenido_pedidos = os.path.join("data_tests_privados", "m", "contenido_pedidos.csv")

        consulta = {
            "funcion": "pizzas_pagables_de_un_tamano",
            "generador_pizzas": {
                "funcion": "pizzas_con_ingrediente",
                "generador_pizzas": {
                    "funcion": "cargar_pizzas",
                    "path": path_pizzas,
                },
                "ingrediente": "tocino",
            },
            "dinero": {
                "funcion": "total_ahorrado_pedidos",
                "generador_contenido_pedidos": {
                    "funcion": "cargar_contenido_pedidos",
                    "path": path_contenido_pedidos,
                },
                "generador_pizzas": {
                    "funcion": "cargar_pizzas",
                    "path": path_pizzas,
                },
            },
            "tamano": "S",
        }

        resultado = consulta_anidada(consulta)

        self.assertIsInstance(resultado, Iterable)

        resultado_esperado = RESULTADO_CONSULTA_ANIDADA_6

        self.assertEqual(list(resultado), resultado_esperado)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que el test funcione para una consulta donde se compren 
        pizzas para los empleados de un Canada.
        """
        path_pizzas = os.path.join("data_tests_privados", "m", "pizzas.csv")
        path_locales = os.path.join("data_tests_privados", "m", "locales.csv")

        consulta = {
            "funcion": "cliente_indeciso",
            "generador_pizzas": {"funcion": "cargar_pizzas", "path": path_pizzas},
            "ingrediente_no_deseado": "anchoas",
            "cantidad_pizzas": {
                "funcion": "cantidad_empleados_pais",
                "generador_locales": {"funcion": "cargar_locales", "path": path_locales},
                "pais": "Chile",
            },
        }

        resultado = consulta_anidada(consulta)

        self.assertIsInstance(resultado, Iterable)

        resultado_esperado = RESULTADO_CONSULTA_ANIDADA_7

        self.assertCountEqual(list(resultado), resultado_esperado)
