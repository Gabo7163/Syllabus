from grafo import Grafo
import pandas as pd
import numpy as np

def cargar_y_limpiar():
    """
    Método que crea un Dataframe a partir de un archivo en formato .csv

    PARTE 1: Debemos completar este método, para realizar los pasos de crear, limpiar los nombres, y limpiar las columnas.
    """
    # Parte 1: leer el archivo CSV
    data = pd.read_csv('database.csv')
    
    # Parte 2: limpiar las columnas 
    ## OPCION 1 usando iloc (usando indices de filas y columnas)
    # data_limpia = data.iloc[:, [1, 5, 3]]
    # data_limpia.columns = ['Nombre', 'Género', 'Rating']

    ## OPCION 2 usando loc (usando los nombres de filas y columnas)
    data_limpia = data.loc[:, ['Nombre', 'Género', 'Rating']]

    # Convertir el tipo de dato a float, usando pandas
    ## OPCION 1
    data_limpia['Rating'] = data_limpia['Rating'].astype(float)
    ## OPCION 2
    # # data_limpia['Rating'] = pd.to_numeric(data_limpia['Rating'], errors='coerce')

    # Parte 3: limpiar los nombres
    ## OPCION 1
    patron = r'[^a-zA-Z0-9\s:,\-"]'
    ## OPCION 2
    # patron = r'[%,!@$&#¡]'
    # Usamos str.replace para aplicar el patrón regex a todos los strings de la columna 'Nombre'
    data_limpia['Nombre'] = data_limpia['Nombre'].str.replace(patron, '', regex=True)

    print("DataFrame de películas:")
    print(data_limpia)
    return data_limpia

def generar_matriz_genero(df):
    """
    Método que crea un Dataframe usando sólo los datos de género de un Dataframe dado.

    PARTE 2.1: Debemos completar este método, usando pandas para crear una nueva matriz que sólo tenga los géneros.
    """
    # Paso 1: Extraemos los generos únicos
    generos_unicos = set()
    for generos_str in df['Género']:
        generos = generos_str.split('|')
        generos_unicos.update(generos)
    generos_unicos = sorted(generos_unicos)

    # Paso 2: Crear la matriz de generos, inicialmente con 0
    matriz_generos = pd.DataFrame(0, index=df.index, columns=generos_unicos)

    # Paso 3: Popular la matriz de géneros
    for idx, generos_str in df['Género'].items():
        generos = generos_str.split('|')
        for genero in generos:
            matriz_generos.at[idx, genero] = 1

    print("\nMatriz de géneros:")
    print(matriz_generos)
    return matriz_generos

def computar_matriz_adyacencia(matriz_generos):
    """
    Método que recibe un Dataframe y usando sus datos genera un array de NumPy.

    PARTE 2.2: Debemos terminar este método, usando NumPy. Primero convertimos el dataframe a un array de Numpy y nos aseguraremos de que sea una matriz de adyacencia para ser usada en grafos. Para eso debemos dejar la diagonal en ceros.
    """
    # Paso 1: Convertir a un array de NumPy
    # array_generos -- class 'numpy.ndarray'
    array_generos = matriz_generos.values

    # Computar la matriz de adyacencia usando el producto punto.
    matriz_adyacencia = np.dot(array_generos, array_generos.T)

    # Paso 2: Dejar la diagonal en ceros. Para asegurarse de que no hayan conexiones entre los mismos nodos.
    np.fill_diagonal(matriz_adyacencia, 0)

    print("\nMatriz de Adyacencia basada en Género:")
    print(matriz_adyacencia)
    return matriz_adyacencia

def crear_lista_adyacencia(df, matriz_adyacencia):
    """
    Método que crea la lista de adyacencia, que se usará luego para crear el grafo.
    """
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

    PARTE 3: Debemos crear el grafo usando la clase Grafo, y agregar sus nodos y aristas correspondientes. Revisar en este punto la clase Grafo para ver como opera.
    """
    # Paso 1: Completar
    grafo = Grafo()
    for nodo, vecinos in lista_adyacencia.items():
        grafo.agregar_nodo(nodo)
        for vecino in vecinos:
            grafo.agregar_nodo(vecino)
            grafo.agregar_arista(nodo, vecino)
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
    metodo_busqueda = 'DFS'  # Escoge entre 'BFS' o 'DFS', prueba!
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
    PARTE 4: Debemos ordenar las recomendaciones por número de géneros compartidos y luego por rating.
    """
    # Paso 1: ordenar las recomendaciones
    recomendaciones.sort(key=lambda x: (-x['Géneros_compartidos'], -x['Rating']))

    # Mostrar recomendaciones
    print(f"\nRecomendaciones basadas en '{nombre_peli}', usando {metodo_busqueda.upper()}:")
    if recomendaciones:
        for idx, rec in enumerate(recomendaciones[:cantidad+1], start=1):
            print(f"{idx}. {rec['Nombre']} (Géneros Compartidos: {rec['Géneros_compartidos']}, Rating: {rec['Rating']})")
    else:
        print("No se encontraron recomendaciones.")