import os
import sys
import unittest
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from tests_privados.solution.test_11 import *
from por_copiar.utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import (
    cargar_contenido_pedidos,
    cargar_pedidos,
    pizza_mas_vendida_del_dia,
)


class TestPizzaMasVendidaDelDiaCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_contenido_pedidos, generador_pedidos, "2024-06-19"
        )

        resultado_esperado = PIZZA_MAS_VENDIDA_DEL_DIA_S_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_contenido_pedidos, generador_pedidos, "2024-08-04"
        )

        resultado_esperado = PIZZA_MAS_VENDIDA_DEL_DIA_S_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_contenido_pedidos, generador_pedidos, "2024-09-05"
        )

        resultado_esperado = PIZZA_MAS_VENDIDA_DEL_DIA_M_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_contenido_pedidos, generador_pedidos, "2024-04-01"
        )

        resultado_esperado = PIZZA_MAS_VENDIDA_DEL_DIA_M_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_contenido_pedidos, generador_pedidos, "2024-05-19"
        )

        resultado_esperado = PIZZA_MAS_VENDIDA_DEL_DIA_M_3

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_contenido_pedidos, generador_pedidos, "2024-01-07"
        )

        resultado_esperado = PIZZA_MAS_VENDIDA_DEL_DIA_L_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_contenido_pedidos, generador_pedidos, "2024-05-21"
        )

        resultado_esperado = PIZZA_MAS_VENDIDA_DEL_DIA_L_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_contenido_pedidos, generador_pedidos, "2024-09-05"
        )

        resultado_esperado = PIZZA_MAS_VENDIDA_DEL_DIA_L_3

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_8(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_contenido_pedidos, generador_pedidos, "2024-02-11"
        )

        resultado_esperado = PIZZA_MAS_VENDIDA_DEL_DIA_L_4

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)
