import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from por_copiar.utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import cantidad_empleados_pais


class TestCantidadEmpleadosPaisCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica funcionamiento correcto cuando no existen locales del país determinado.
        """
        Local = namedtuple(
            "Local",
            ["id_local", "direccion", "pais", "ciudad", "cantidad_trabajadores"],
        )

        lista_entregada = [
            Local(
                id_local=1,
                direccion="85024 Valerie link Tunnel Apt. 363",
                pais="Argentina",
                ciudad="Hillhaven",
                cantidad_trabajadores=3,
            ),
            Local(
                id_local=2,
                direccion="3896 Garza Brooks jardines",
                pais="Slovenia",
                ciudad="North Trevor",
                cantidad_trabajadores=9,
            ),
            Local(
                id_local=3,
                direccion="Calle Falsa 101",
                pais="Chile",
                ciudad="Santiago",
                cantidad_trabajadores=6,
            ),
            Local(
                id_local=4,
                direccion="Calle Fake 12226",
                pais="Chile",
                ciudad="Valdivia",
                cantidad_trabajadores=4,
            ),
            Local(
                id_local=5,
                direccion="Calle Falsa 127",
                pais="Argentina",
                ciudad="Santiago",
                cantidad_trabajadores=2,
            ),
        ]

        generador_entregado_locales = (asociacion for asociacion in lista_entregada)

        int_estudiante = cantidad_empleados_pais(
            generador_entregado_locales, "Finlandia"
        )

        self.assertIsInstance(int_estudiante, (int))

        int_esperado = 0

        self.assertEqual(int_estudiante, int_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica funcionamiento correcto cuando existe solamente un local del país determinado y solo un empleado.
        """
        Local = namedtuple(
            "Local",
            ["id_local", "direccion", "pais", "ciudad", "cantidad_trabajadores"],
        )

        lista_entregada = [
            Local(
                id_local=1,
                direccion="85024 Valerie link Tunnel Apt. 363",
                pais="Uzbekistan",
                ciudad="Hillhaven",
                cantidad_trabajadores=1,
            ),
            Local(
                id_local=2,
                direccion="3896 Garza Brooks jardines",
                pais="Slovenia",
                ciudad="North Trevor",
                cantidad_trabajadores=1,
            ),
            Local(
                id_local=3,
                direccion="Calle Falsa 101",
                pais="Bulgaria",
                ciudad="Ciudad",
                cantidad_trabajadores=1,
            ),
            Local(
                id_local=4,
                direccion="Calle Fake 12226",
                pais="Sloth",
                ciudad="Valdivia",
                cantidad_trabajadores=13,
            ),
            Local(
                id_local=5,
                direccion="Calle Falsa 127",
                pais="Ecuador",
                ciudad="Santiago",
                cantidad_trabajadores=21,
            ),
        ]

        generador_entregado_locales = (asociacion for asociacion in lista_entregada)

        int_estudiante = cantidad_empleados_pais(
            generador_entregado_locales, "Bulgaria"
        )

        self.assertIsInstance(int_estudiante, (int))

        int_esperado = 1

        self.assertEqual(int_estudiante, int_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica funcionamiento correcto cuando existe solamente un local del país determinado y dos o más empleados.
        """
        Local = namedtuple(
            "Local",
            ["id_local", "direccion", "pais", "ciudad", "cantidad_trabajadores"],
        )

        lista_entregada = [
            Local(
                id_local=1,
                direccion="85024 Valerie link Tunnel Apt. 363",
                pais="Uzbekistafn",
                ciudad="Hillhaven",
                cantidad_trabajadores=3,
            ),
            Local(
                id_local=2,
                direccion="3896 Garza Brooks jardines",
                pais="Slovenia",
                ciudad="North Trevor",
                cantidad_trabajadores=1,
            ),
            Local(
                id_local=3,
                direccion="Calle Falsa 101",
                pais="Chile",
                ciudad="Santiago",
                cantidad_trabajadores=6,
            ),
            Local(
                id_local=4,
                direccion="Calle C 2226",
                pais="TN",
                ciudad="Random.choice()",
                cantidad_trabajadores=11,
            ),
            Local(
                id_local=5,
                direccion="Calle Falsa 127",
                pais="Croatia",
                ciudad="Santiago",
                cantidad_trabajadores=25463,
            ),
            Local(
                id_local=6,
                direccion="Cal INSERT el 213",
                pais="Croacia",
                ciudad="Santiago",
                cantidad_trabajadores=23213,
            ),
        ]

        generador_entregado_locales = (asociacion for asociacion in lista_entregada)

        int_estudiante = cantidad_empleados_pais(generador_entregado_locales, "TN")

        self.assertIsInstance(int_estudiante, (int))

        int_esperado = 11

        self.assertEqual(int_estudiante, int_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica funcionamiento correcto cuando existen dos o más locales del país determiando y en cada local dos o más empleados.
        """
        Local = namedtuple(
            "Local",
            ["id_local", "direccion", "pais", "ciudad", "cantidad_trabajadores"],
        )

        lista_entregada = [
            Local(
                id_local=1,
                direccion="85024 Valerie link Tunnel Apt. 363",
                pais="Drop Table",
                ciudad="Hillhaven",
                cantidad_trabajadores=3,
            ),
            Local(
                id_local=2,
                direccion="3896 Garza Brooks jardines",
                pais="drop table",
                ciudad="North Trevor",
                cantidad_trabajadores=1,
            ),
            Local(
                id_local=3,
                direccion="Calle Falsa 13201",
                pais="DROP TABLE",
                ciudad="Santiago",
                cantidad_trabajadores=64,
            ),
            Local(
                id_local=4,
                direccion="Calle Fake 12226",
                pais="DROP TABLE",
                ciudad="Valdivia",
                cantidad_trabajadores=131,
            ),
            Local(
                id_local=5,
                direccion="Calle Falsa 127",
                pais="DROP TABLE",
                ciudad="El futuro es hoy, ¿o no?",
                cantidad_trabajadores=25346,
            ),
            Local(
                id_local=6,
                direccion="Cal el 213",
                pais="DROP TABLE VERSION PRIMITIVA",
                ciudad="FAs0111100000111111111111111110e322dsa",
                cantidad_trabajadores=233243,
            ),
            Local(
                id_local=7,
                direccion="Calle Falsa 123427",
                pais="DROP TABLE 1.3.423",
                ciudad="Steve",
                cantidad_trabajadores=2,
            ),
            Local(
                id_local=8,
                direccion="Calle Falsa 123427",
                pais="DROP TABLE",
                ciudad="Steve",
                cantidad_trabajadores=2,
            ),
        ]

        generador_entregado_locales = (asociacion for asociacion in lista_entregada)

        int_estudiante = cantidad_empleados_pais(
            generador_entregado_locales, "DROP TABLE"
        )

        self.assertIsInstance(int_estudiante, (int))

        int_esperado = 25543

        self.assertEqual(int_estudiante, int_esperado)
