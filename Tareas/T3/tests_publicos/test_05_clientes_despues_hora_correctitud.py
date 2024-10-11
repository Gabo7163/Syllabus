import os
import sys
import unittest
from collections import namedtuple

from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_05 import *
from utilidades import N_SECOND

from consultas import clientes_despues_hora



class TestClientesDespuesHoraCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que el test funcione si es que no hay clientes después de esa hora
        """

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=2, fecha="2021-01-01", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=3, fecha="2021-01-01", hora="11:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=4, fecha="2021-01-01", hora="10:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = clientes_despues_hora(generador_entregado, "14:00")

        self.assertIsInstance(resultado_estudiante, (str))

        lista_estudiante = []
        if resultado_estudiante != "":
            lista_estudiante = resultado_estudiante.split(" ")

        lista_esperada = []

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que el test funcione si es que todos los clientes son después de esa hora
        """

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=2, fecha="2021-01-01", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=3, fecha="2021-01-01", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=4, fecha="2021-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = clientes_despues_hora(generador_entregado, "12:00")

        self.assertIsInstance(resultado_estudiante, (str))

        lista_estudiante = []
        if resultado_estudiante != "":
            lista_estudiante = resultado_estudiante.split(" ")

        lista_esperada = ["1", "2", "3", "4", "5", "6"]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que el test funcione si es que el generador es vacío
        """

        lista_entregada = []

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = clientes_despues_hora(generador_entregado, "12:00")

        self.assertIsInstance(resultado_estudiante, (str))

        lista_estudiante = []
        if resultado_estudiante != "":
            lista_estudiante = resultado_estudiante.split(" ")

        lista_esperada = []

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que el test funcione si es que hay un solo cliente después de esa hora
        """

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=2, fecha="2021-01-01", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=3, fecha="2021-01-01", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=4, fecha="2021-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = clientes_despues_hora(generador_entregado, "18:00")

        self.assertIsInstance(resultado_estudiante, (str))

        lista_estudiante = []
        if resultado_estudiante != "":
            lista_estudiante = resultado_estudiante.split(" ")

        lista_esperada = ["4"]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que el test funcione si es que la hora dada no termina en :00
        """

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=2, fecha="2021-01-01", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=3, fecha="2021-01-01", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=4, fecha="2021-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = clientes_despues_hora(generador_entregado, "17:30")

        self.assertIsInstance(resultado_estudiante, (str))

        lista_estudiante = []
        if resultado_estudiante != "":
            lista_estudiante = resultado_estudiante.split(" ")

        lista_esperada = ["4"]

        self.assertCountEqual(lista_estudiante, lista_esperada)
