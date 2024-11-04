from collections import namedtuple

# ----------------------------------------------------------------------------
# NO MODIFICAR
# ----------------------------------------------------------------------------

Pizzas = namedtuple("Pizzas", "nombre ingredientes precio")
Locales = namedtuple("Locales", "id_local direccion pais ciudad cantidad_trabajadores")
ContenidoPedidos = namedtuple("ContenidoPedidos", "id_pedido nombre cantidad descuento")
Pedidos = namedtuple("Pedidos", "id_pedido id_local id_cliente fecha hora")

N_SECOND = 30
