import os
import sys
import unittest
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from tests_privados.solution.test_01 import *
from por_copiar.utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import cargar_contenido_pedidos, pedidos_con_al_menos_esta_pizza



class TestPedidoConAlMenosEstaPizzaCargaDeDatos(unittest.TestCase):

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

        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(g_pe, "Pepinillos y Tocino")


        resultado_esperado = PEDIDOS_CON_AL_MENOS_ESTA_PIZZA_S_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")

        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            g_pe, "Queso de Cabra y Pimientos"
        )

        resultado_esperado = PEDIDOS_CON_AL_MENOS_ESTA_PIZZA_S_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            g_pe, "Vibrante Vibrante Increíble con Originalidad"
        )

        resultado_esperado = PEDIDOS_CON_AL_MENOS_ESTA_PIZZA_M_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            g_pe, "Jugoso Sensacional Cremoso con Frescura"
        )

        resultado_esperado = PEDIDOS_CON_AL_MENOS_ESTA_PIZZA_M_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            g_pe, "Dorado Perfecto Radiante con Magia"
        )

        resultado_esperado = PEDIDOS_CON_AL_MENOS_ESTA_PIZZA_M_3

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            g_pe, "Tentador Sublime Envolvente con Toque Divino"
        )

        resultado_esperado = PEDIDOS_CON_AL_MENOS_ESTA_PIZZA_L_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            g_pe, "Picante Crujiente Fresco con Delicadeza"
        )

        resultado_esperado = PEDIDOS_CON_AL_MENOS_ESTA_PIZZA_L_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            g_pe, "Cremoso Tierno Tentador con Pureza"
        )

        resultado_esperado = PEDIDOS_CON_AL_MENOS_ESTA_PIZZA_L_3

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_8(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            g_pe, "Vibrante Asombroso Envolvente con Estilo"
        )

        resultado_esperado = PEDIDOS_CON_AL_MENOS_ESTA_PIZZA_L_4

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_9(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño XL.
        """
        carpeta = "xl"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        print("path", path)
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            g_pe, "Jugoso Esponjoso Crujiente con Originalidad"
        )

        resultado_esperado = PEDIDOS_CON_AL_MENOS_ESTA_PIZZA_XL_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)
