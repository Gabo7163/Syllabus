import os
import sys
import unittest
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from tests_privados.solution.test_05 import *
from por_copiar.utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import cargar_pedidos, clientes_despues_hora



class TestClientesDespuesHoraCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")

        g_a = cargar_pedidos(path)

        resultado_estudiante = clientes_despues_hora(g_a, "19:00")

        resultado_esperado = CLIENTES_DESPUES_HORA_S_1

        lista_esperada = resultado_esperado.split(" ")

        lista_estudiante = resultado_estudiante.split(" ")

        self.assertIsInstance(resultado_estudiante, (str))

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_a = cargar_pedidos(path)

        resultado_estudiante = clientes_despues_hora(g_a, "23:30")

        resultado_esperado = CLIENTES_DESPUES_HORA_S_2

        lista_esperada = resultado_esperado.split(" ")

        lista_estudiante = resultado_estudiante.split(" ")

        self.assertIsInstance(resultado_estudiante, (str))

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_a = cargar_pedidos(path)

        resultado_estudiante = clientes_despues_hora(g_a, "16:00")

        resultado_esperado = CLIENTES_DESPUES_HORA_M_1

        lista_esperada = resultado_esperado.split(" ")

        lista_estudiante = resultado_estudiante.split(" ")

        self.assertIsInstance(resultado_estudiante, (str))

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_a = cargar_pedidos(path)

        resultado_estudiante = clientes_despues_hora(g_a, "22:00")

        resultado_esperado = CLIENTES_DESPUES_HORA_M_2

        lista_esperada = resultado_esperado.split(" ")

        lista_estudiante = resultado_estudiante.split(" ")

        self.assertIsInstance(resultado_estudiante, (str))

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_a = cargar_pedidos(path)

        resultado_estudiante = clientes_despues_hora(g_a, "20:00")

        resultado_esperado = CLIENTES_DESPUES_HORA_M_3

        lista_esperada = resultado_esperado.split(" ")

        lista_estudiante = resultado_estudiante.split(" ")

        self.assertIsInstance(resultado_estudiante, (str))

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_a = cargar_pedidos(path)

        resultado_estudiante = clientes_despues_hora(g_a, "23:10")

        resultado_esperado = CLIENTES_DESPUES_HORA_L_1

        lista_esperada = resultado_esperado.split(" ")

        lista_estudiante = resultado_estudiante.split(" ")

        self.assertIsInstance(resultado_estudiante, (str))

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_a = cargar_pedidos(path)

        resultado_estudiante = clientes_despues_hora(g_a, "23:55")

        resultado_esperado = CLIENTES_DESPUES_HORA_L_2

        lista_esperada = resultado_esperado.split(" ")

        lista_estudiante = resultado_estudiante.split(" ")

        self.assertIsInstance(resultado_estudiante, (str))

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_a = cargar_pedidos(path)

        resultado_estudiante = clientes_despues_hora(g_a, "23:33")

        resultado_esperado = CLIENTES_DESPUES_HORA_L_3

        lista_esperada = resultado_esperado.split(" ")

        lista_estudiante = resultado_estudiante.split(" ")

        self.assertIsInstance(resultado_estudiante, (str))

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_8(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_a = cargar_pedidos(path)

        resultado_estudiante = clientes_despues_hora(g_a, "22:48")

        resultado_esperado = CLIENTES_DESPUES_HORA_L_4

        lista_esperada = resultado_esperado.split(" ")

        lista_estudiante = resultado_estudiante.split(" ")

        self.assertIsInstance(resultado_estudiante, (str))

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_9(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño XL.
        """
        carpeta = "xl"

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_a = cargar_pedidos(path)

        resultado_estudiante = clientes_despues_hora(g_a, "23:57")

        resultado_esperado = CLIENTES_DESPUES_HORA_XL_1

        lista_esperada = resultado_esperado.split(" ")

        lista_estudiante = resultado_estudiante.split(" ")

        self.assertIsInstance(resultado_estudiante, (str))

        self.assertCountEqual(lista_estudiante, lista_esperada)
