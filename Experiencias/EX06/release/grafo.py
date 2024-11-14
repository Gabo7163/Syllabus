from collections import deque

class Grafo:
    """
    Clase que representa nuestro grafo principal.
    Sus métodos pueden agregar nodos y aristas, como también realizar búsqueda en dos algoritmos distintos: BFS y DFS.
    """
    def __init__(self):
        self.lista_adyacencia = {}

    def agregar_nodo(self, nodo):
        if nodo not in self.lista_adyacencia:
            self.lista_adyacencia[nodo] = []

    def agregar_arista(self, nodo1, nodo2):
        # Primero hay que asegurarse si ambos existen
        if nodo1 not in self.lista_adyacencia:
            self.agregar_nodo(nodo1)
        if nodo2 not in self.lista_adyacencia:
            self.agregar_nodo(nodo2)

        # Para evitar duplicados! Muy importante
        if nodo2 not in self.lista_adyacencia[nodo1]:
            self.lista_adyacencia[nodo1].append(nodo2)
        if nodo1 not in self.lista_adyacencia[nodo2]:
            self.lista_adyacencia[nodo2].append(nodo1)

    def recomendacion_bfs(self, pelicula_incial, maxima_profundidad=2):
        if pelicula_incial not in self.lista_adyacencia:
            print(f"Película: '{pelicula_incial}' no encontrada en el grafo.")
            return []

        visitado = set()
        queue = deque()
        profundidad = {pelicula_incial: 0}
        recomendaciones = []

        visitado.add(pelicula_incial)
        queue.append(pelicula_incial)

        while queue:
            pelicula_actual = queue.popleft()
            profundidad_actual = profundidad[pelicula_actual]

            if profundidad_actual < maxima_profundidad:
                for vecino in self.lista_adyacencia[pelicula_actual]:
                    if vecino not in visitado:
                        visitado.add(vecino)
                        queue.append(vecino)
                        profundidad[vecino] = profundidad_actual + 1
                        if vecino != pelicula_incial:
                            recomendaciones.append(vecino)

        # Se remueven los duplicados
        return list(set(recomendaciones))

    def recomendacion_dfs(self, pelicula_incial, maxima_profundidad=2):
        if pelicula_incial not in self.lista_adyacencia:
            print(f"Pelicula: '{pelicula_incial}' no encontrada en el grafo.")
            return []

        visitado = set()
        recomendaciones = []

        def dfs_recursive(pelicula_actual, profundidad_actual):
            if profundidad_actual > maxima_profundidad:
                return
            visitado.add(pelicula_actual)
            for vecino in self.lista_adyacencia[pelicula_actual]:
                if vecino not in visitado:
                    # No considerar la película incial
                    if vecino != pelicula_incial:
                        recomendaciones.append(vecino)
                    dfs_recursive(vecino, profundidad_actual + 1)

        dfs_recursive(pelicula_incial, 0)
        # Se remueven los duplicados
        return list(set(recomendaciones))
