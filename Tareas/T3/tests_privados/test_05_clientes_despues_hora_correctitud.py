import os
import sys
import unittest
from collections import namedtuple

from tests_privados.timeout_function import timeout
from tests_privados.solution.test_05 import *
from utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

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
                id_pedido=1, id_local=1, id_cliente=14, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=2, id_cliente=21, fecha="2021-01-01", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=6, id_cliente=33, fecha="2021-01-01", hora="11:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=8, id_cliente=47, fecha="2021-01-01", hora="10:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=10, id_cliente=51, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=11, id_cliente=67, fecha="2021-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = clientes_despues_hora(generador_entregado, "15:00")

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
                id_pedido=1, id_local=14, id_cliente=71, fecha="2021-01-02", hora="16:30:00"
            ),
            Pedido(
                id_pedido=2, id_local=17, id_cliente=5, fecha="2021-01-01", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=15, id_cliente=33, fecha="2021-01-03", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=13, id_cliente=44, fecha="2021-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=17, id_cliente=75, fecha="2021-01-01", hora="17:34:00"
            ),
            Pedido(
                id_pedido=6, id_local=10, id_cliente=96, fecha="2021-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = clientes_despues_hora(generador_entregado, "13:00")

        self.assertIsInstance(resultado_estudiante, (str))

        lista_estudiante = []
        if resultado_estudiante != "":
            lista_estudiante = resultado_estudiante.split(" ")

        lista_esperada = ["71", "33", "44", "75", "96"]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que el test funcione si es que el generador es vacío
        """

        lista_entregada = []

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = clientes_despues_hora(generador_entregado, "15:00")

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
                id_pedido=1, id_local=31, id_cliente=1, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=14, id_cliente=22, fecha="2021-01-01", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=21, id_cliente=35, fecha="2021-01-01", hora="22:30:00"
            ),
            Pedido(
                id_pedido=4, id_local=81, id_cliente=45, fecha="2021-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=91, id_cliente=577, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=14, id_cliente=60, fecha="2021-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = clientes_despues_hora(generador_entregado, "22:00")

        self.assertIsInstance(resultado_estudiante, (str))

        lista_estudiante = []
        if resultado_estudiante != "":
            lista_estudiante = resultado_estudiante.split(" ")

        lista_esperada = ["35"]

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
                id_pedido=1, id_local=51, id_cliente=18, fecha="2021-01-01", hora="02:00:00"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=32, fecha="2021-01-01", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=21, id_cliente=49, fecha="2021-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=2, id_local=71, id_cliente=23, fecha="2021-01-01", hora="09:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=71, id_cliente=55, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=19, id_cliente=64, fecha="2021-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = clientes_despues_hora(generador_entregado, "10:30")

        self.assertIsInstance(resultado_estudiante, (str))

        lista_estudiante = []
        if resultado_estudiante != "":
            lista_estudiante = resultado_estudiante.split(" ")

        lista_esperada = ["32", "49", "55", "64"]

        self.assertCountEqual(lista_estudiante, lista_esperada)
