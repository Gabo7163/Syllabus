class Node:
    id_counter = 0  # id_counter como variable de clase para asegurar IDs únicos

    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.id = Node.id_counter
        Node.id_counter += 1  # Incrementa el contador global de IDs para cada nodo

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def __str__(self):
        return f'Node {self.id}: {self.value}'
    
    def __repr__(self):
        return f'Node {self.id}: {self.value}'

    def __eq__(self, other):
        return isinstance(other, Node) and self.id == other.id

    def __hash__(self):
        return hash(self.id)


class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, node1, node2):
        node1.add_neighbor(node2)
        node2.add_neighbor(node1)

    def dfs(self, start):
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                print(node)  # Mostrar el nodo visitado
                visited.add(node)
                # Agrega los vecinos no visitados al stack
                stack.extend([neighbor for neighbor in node.neighbors if neighbor not in visited])
        return visited

    def bfs(self, start):
        visited = set()
        queue = [start]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node)  # Mostrar el nodo visitado
                visited.add(node)
                # Agrega los vecinos no visitados a la cola
                queue.extend([neighbor for neighbor in node.neighbors if neighbor not in visited])
        return visited

    def __str__(self):
        return ', '.join(str(node) for node in self.nodes)


# # Reiniciar el contador de IDs para Node
# Node.id_counter = 0

# # Ejemplo 1: Árbol sin ciclos
# a = Node("A")
# b = Node("B")
# c = Node("C")
# d = Node("D")
# e = Node("E")

# graph = Graph()
# graph.add_node(a)
# graph.add_node(b)
# graph.add_node(c)
# graph.add_node(d)
# graph.add_node(e)

# graph.add_edge(a, b)
# graph.add_edge(a, c)
# graph.add_edge(b, d)
# graph.add_edge(b, e)

# print("DFS (árbol sin ciclo):")
# graph.dfs(d)
# print("\nBFS (árbol sin ciclo):")
# graph.bfs(d)

# # Ejemplo 2: Grafo con ciclos
# graph.add_edge(e, c)

# print("\nDFS (grafo con ciclo):")
# graph.dfs(d)
# print("\nBFS (grafo con ciclo):")
# graph.bfs(d)
