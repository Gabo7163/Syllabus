from grafo import Grafo
import pandas as pd
import numpy as np
import re

def cargar_y_limpiar():
    """
    Método que crea un Dataframe a partir de un archivo en formato .csv

    PARTE 1: Debemos completar este método, para realizar los pasos de crear, limpiar los nombres, y limpiar las columnas.
    """
    # Parte 1 TODO: leer el archivo CSV

    # Parte 2 TODO: limpiar las columnas

    # Parte 3 TODO: limpiar los nombres

    print("DataFrame de películas:")
    print(data_limpia)
    return data_limpia

def generar_matriz_genero(df):
    """
    Método que crea un Dataframe a partir de un archivo en formato .csv

    PARTE 2.1: Debemos completar este método, usando pandas para crear una nueva matriz que sólo tenga los géneros.
    """
    # TODO: completar

    print("\nMatriz de géneros:")
    print(matriz_generos)
    return matriz_generos

def computar_matriz_adyacencia(matriz_generos):
    """
    Método que crea un Dataframe a partir de un archivo en formato .csv

    PARTE 2.2: Debemos terminar este método, usando NumPy. Primero convertimos el dataframe a un array de Numpy y nos aseguraremos de que sea una matriz de adyacencia para ser usada en grafos.
    """
    # Paso 1 TODO: Convertir matriz a un array de NumPy.


    # Computar la matriz de adyacencia usando el producto punto.
    matriz_adyacencia = np.dot(array_generos, array_generos.T)

    # Paso 2 TODO: Dejar la diagonal en ceros. Para asegurarse de que no hayan conexiones entre los mismos nodos.

    print("\nMatriz de Adyacencia basada en Género:")
    print(matriz_adyacencia)
    return matriz_adyacencia

def crear_lista_adyacencia(df, matriz_adyacencia):
    # NO MODIFICAR
    nombres_peliculas = df['Nombre'].tolist()
    lista_adyacencia = {}

    for i, pelicula in enumerate(nombres_peliculas):
        peliculas_conectadas = []
        for j, fuerza_conexion in enumerate(matriz_adyacencia[i]):
            if fuerza_conexion > 0:
                peliculas_conectadas.append(nombres_peliculas[j])
        lista_adyacencia[pelicula] = peliculas_conectadas

    return lista_adyacencia

def crear_grafo(lista_adyacencia):
    """
    Método que crea un grafo, instanciando un objeto de la clase Grafo, a partir de la lista de adyacencia creada en el método anterior.

    PARTE 3: Debemos crear el grafo usando la clase Grafo, y agregar sus nodos y aristas correspondientes.
    """
    # Paso 1 TODO: completar
    return grafo

if __name__ == "__main__":
    df = cargar_y_limpiar()
    input(15 * "*" + "\n> Presiona enter para seguir")
    matriz_generos = generar_matriz_genero(df)
    input(15 * "*" + "\n> Presiona enter para seguir")
    matriz_adyacencia = computar_matriz_adyacencia(matriz_generos)
    lista_adyacencia = crear_lista_adyacencia(df, matriz_adyacencia)
    
    # Creamos el grafo
    graph = crear_grafo(lista_adyacencia)

    # Parámetros de configuración
    nombre_peli = 'Snowden'  # Puedes cambiarlo, prueba!
    metodo_busqueda = 'DFS'  # Escoge entre 'BFS' o 'DFS'
    profundidad = 2  # Qué tan profundo buscar, prueba!
    cantidad = 5 # Top 5 recomendaciones
    
    # Generar la búsqueda
    if metodo_busqueda.upper() == 'BFS':
        peliculas_recomendadas = graph.recomendacion_bfs(nombre_peli,maxima_profundidad=profundidad)
    elif metodo_busqueda.upper() == 'DFS':
        peliculas_recomendadas = graph.recomendacion_dfs(nombre_peli,maxima_profundidad=profundidad)

    # Recolectar las recomendaciones
    recomendaciones = []
    generos_peliculas = set(df[df['Nombre'] == nombre_peli]['Género'].values[0].split('|'))

    for otra_pelicula in peliculas_recomendadas:
        otra_pelicula_genero = set(df[df['Nombre'] == otra_pelicula]['Género'].values[0].split('|'))
        generos_compartidos = generos_peliculas.intersection(otra_pelicula_genero)
        cant_generos_compartidos = len(generos_compartidos)
        rating = df[df['Nombre'] == otra_pelicula]['Rating'].values[0]
        recomendaciones.append({
            'Nombre': otra_pelicula,
            'Géneros_compartidos': cant_generos_compartidos,
            'Rating': rating
        })

    input(15 * "*" + "\n> Presiona enter para seguir")
    """
    ¡Extra!

    PARTE 4: Debemos ordenar las recomendaciones por número de géneros compartidos y luego por rating.
    """
    # Paso 1 TODO: ordenar las recomendaciones

    # Mostrar recomendaciones
    print(f"\nRecomendaciones basadas en '{nombre_peli}', usando {metodo_busqueda.upper()}:")
    if recomendaciones:
        for idx, rec in enumerate(recomendaciones[:cantidad+1], start=1):
            print(f"{idx}. {rec['Nombre']} (Géneros Compartidos: {rec['Géneros_compartidos']}, Rating: {rec['Rating']})")
    else:
        print("No se encontraron recomendaciones.")