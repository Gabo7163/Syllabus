import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from por_copiar.utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import popularidad_mezcla_de_ingredientes


class TestPopularidadMezclaDeIngredientesCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica funcionamiento correcto cuando no existe ningún ingrediente del set en las pizzas.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Marga_XL",
                ingredientes="tomate;queso;invención;albahaca",
                precio=28000,
            ),
            Pizza(
                nombre="Napolif_S",
                ingredientes="ficción;tomate;jamón;salame",
                precio=7100,
            ),
            Pizza(
                nombre="Hawaiana_XL",
                ingredientes="tomate;queso;jamón;piña;salsa",
                precio=29290,
            ),
            Pizza(
                nombre="Pepperoni_L",
                ingredientes="tomate;queso;pepperoni;huevos",
                precio=8000,
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo BBQ_L",
                ingredientes="tomate;queso;pollo;cebolla;bbq;pepinillos",
                precio=7200,
            ),
        ]

        generador_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(id_pedido=1, nombre="Marga_XL", cantidad=4, descuento=0.0),
            ContenidoPedido(
                id_pedido=2, nombre="Napolif_S", cantidad=10, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_Normal_M", cantidad=6, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiana_XL", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Pepperoni_L", cantidad=30, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Pollo BBQ_L", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Vegetariana_S", cantidad=4, descuento=0.0
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        int_estudiante = popularidad_mezcla_de_ingredientes(
            generador_pizzas,
            generador_entregado_pedidos,
            {"deseos", "logros", "sueños", "esperanzas"},
        )

        self.assertIsInstance(int_estudiante, (int))

        int_esperado = 0

        self.assertEqual(int_estudiante, int_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica funcionamiento correcto cuando no existe la combinación de ingredientes determinados en las pizzas (pero sí al menos un ingrediente en alguna pizza).
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Marga_XL", ingredientes="tomate;queso;albahaca", precio=28000
            ),
            Pizza(nombre="Napolif_S", ingredientes="tomate;jamón;salame", precio=7100),
            Pizza(
                nombre="Hawaiana_XL",
                ingredientes="tomate;queso;jamón",
                precio=29290,
            ),
            Pizza(
                nombre="Pepperoni_L", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;pepinillos;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo BBQ_L",
                ingredientes="tomate;queso;pollo;cebolla;bbq;pepinillos",
                precio=7200,
            ),
        ]

        generador_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(id_pedido=1, nombre="Marga_XL", cantidad=4, descuento=0.0),
            ContenidoPedido(
                id_pedido=2, nombre="Napolif_S", cantidad=10, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_Normal_M", cantidad=6, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiana_XL", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Pepperoni_L", cantidad=30, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Pollo BBQ_L", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Vegetariana_S", cantidad=4, descuento=0.0
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        int_estudiante = popularidad_mezcla_de_ingredientes(
            generador_pizzas,
            generador_entregado_pedidos,
            {"albahaca", "queso", "pepinillos"},
        )

        self.assertIsInstance(int_estudiante, (int))

        int_esperado = 0

        self.assertEqual(int_estudiante, int_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica funcionamiento correcto cuando solamente una pizza vendida cumple con tener todos los ingredientes determinados.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Marga_XL", ingredientes="tomate;queso;albahaca", precio=28000
            ),
            Pizza(nombre="Napolif_S", ingredientes="tomate;jamón;salame", precio=7100),
            Pizza(
                nombre="Hawaiana_XL",
                ingredientes="tomate;queso;jamón;piña",
                precio=29290,
            ),
            Pizza(
                nombre="Pepperoni_L", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas;salsa",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo BBQ_L",
                ingredientes="tomate;queso;pollo;cebolla;bbq;pepinillos;salsa",
                precio=7200,
            ),
            Pizza(
                nombre="Vegetariana_M",
                ingredientes="salsa;tomate;queso;champiñones;aceitunas;uvas",
                precio=28000,
            ),
        ]

        generador_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(id_pedido=7, nombre="Marga_XL", cantidad=4, descuento=0.0),
            ContenidoPedido(
                id_pedido=2, nombre="Napolif_S", cantidad=10, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiana_XL", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Pepperoni_L", cantidad=30, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Pollo BBQ_L", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=1, nombre="Vegetariana_S", cantidad=4321, descuento=0.0
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        int_estudiante = popularidad_mezcla_de_ingredientes(
            generador_pizzas,
            generador_entregado_pedidos,
            {"tomate", "queso", "champiñones", "pimentón", "salsa"},
        )

        self.assertIsInstance(int_estudiante, (int))

        int_esperado = 4321

        self.assertEqual(int_estudiante, int_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica funcionamiento correcto cuando dos o más pizzas vendidas cumplen con tener todos los ingredientes determinados.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Marga_XL", ingredientes="tomate;queso;albahaca", precio=28000
            ),
            Pizza(nombre="Napolif_S", ingredientes="tomate;jamón;salame", precio=7100),
            Pizza(
                nombre="Hawaiana_XL",
                ingredientes="tomate;queso;jamón;piña",
                precio=29290,
            ),
            Pizza(
                nombre="Pepperoni_L", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="champiñones;pimentón;aceitunas;salsa;queso",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo BBQ_L",
                ingredientes="pollo;tomate;cebolla;bbq;pepinillos",
                precio=7200,
            ),
            Pizza(
                nombre="Vegetariana_M",
                ingredientes="tomate;champiñones;aceitunas;uvas",
                precio=28000,
            ),
        ]

        generador_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(id_pedido=1, nombre="Marga_XL", cantidad=4, descuento=0.0),
            ContenidoPedido(
                id_pedido=2, nombre="Napolif_S", cantidad=54326, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_S", cantidad=674523, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiana_XL", cantidad=432, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Pepperoni_L", cantidad=6546, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Pollo BBQ_L", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Vegetariana_M", cantidad=5431, descuento=0.0
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        int_estudiante = popularidad_mezcla_de_ingredientes(
            generador_pizzas,
            generador_entregado_pedidos,
            {"tomate", "queso"},
        )

        self.assertIsInstance(int_estudiante, (int))

        int_esperado = 6982

        self.assertEqual(int_estudiante, int_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica funcionamiento correcto se tienen ingredientes que son substrings de otros ingredientes.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Marga_XL",
                ingredientes="tomate;Lu Salsa de SUBSTRING XDDD;queso;albahaca;La Salsa",
                precio=28000,
            ),
            Pizza(
                nombre="OP Napolif_S",
                ingredientes="Lu;tomate;jamón;Salsa;Lu Salsa de SUBSTRING;salame;de;SUBSTRING;champiñones",
                precio=7100,
            ),
            Pizza(
                nombre="Hawaiana_XL",
                ingredientes="tomate;salsa de champiñones 100%;La;queso;jamón;Lu Salsa de SUBSTRING;piña;frambuesa;La Salsa de;palta;salame;tocino;champiño",
                precio=29290,
            ),
            Pizza(
                nombre="Pepperoni_L",
                ingredientes="tomate;champiñones ;Lu Salsa;queso;pepperoni;salsa de champiñones;",
                precio=8000,
            ),
            Pizza(
                nombre="Pollo BBQ_S",
                ingredientes="Lu Salsa de;champiñones;pimentón;Lu Salsa de SUBSTRING XDDD ULTRA MEGA PODER;aceitunas;salsa;champi",
                precio=9000,
            ),
            Pizza(
                nombre="Mega Pollo BBQ_L",
                ingredientes="pollo;cebolla;Lu Salsa de SUBSTRING;bbq;champiñones;pepinillos;TOMATE;piña",
                precio=7200,
            ),
            Pizza(
                nombre="S Vegetariana_M",
                ingredientes="Lu Salsa de SUBSTRING;tomate;queso;champiñones;pear;aceitunas;uvas;piñal",
                precio=28000,
            ),
        ]

        generador_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(id_pedido=1, nombre="Marga_XL", cantidad=4, descuento=0.0),
            ContenidoPedido(
                id_pedido=2, nombre="OP Napolif_S", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_S", cantidad=3, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiana_XL", cantidad=421, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Pepperoni_L", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Mega Pollo BBQ_L", cantidad=16, descuento=0.4321
            ),
            ContenidoPedido(
                id_pedido=7, nombre="S Vegetariana_M", cantidad=56536, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Pollo BBQ_S", cantidad=400050, descuento=0.3897238
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        int_estudiante = popularidad_mezcla_de_ingredientes(
            generador_pizzas,
            generador_entregado_pedidos,
            {"Lu Salsa de SUBSTRING", "piña"},
        )

        self.assertIsInstance(int_estudiante, (int))

        int_esperado = 437

        self.assertEqual(int_estudiante, int_esperado)
