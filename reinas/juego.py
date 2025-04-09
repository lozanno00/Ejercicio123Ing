def es_seguro(tablero, fila, columna, n):
    """Verifica si es seguro colocar una reina en la posición dada."""
    # Verificar la columna
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False

    # Verificar la diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False

    # Verificar la diagonal superior derecha
    for i, j in zip(range(fila, -1, -1), range(columna, n)):
        if tablero[i][j] == 1:
            return False

    return True

def resolver_reinas(tablero, fila, n):
    """Resuelve el problema de las N reinas usando backtracking."""
    if fila >= n:
        return True

    for columna in range(n):
        if es_seguro(tablero, fila, columna, n):
            tablero[fila][columna] = 1
            if resolver_reinas(tablero, fila + 1, n):
                return True
            tablero[fila][columna] = 0  # Backtracking

    return False

def iniciar_tablero(n):
    """Inicializa un tablero vacío de tamaño n x n."""
    return [[0 for _ in range(n)] for _ in range(n)]

def n_reinas(n):
    """Resuelve el problema de las N reinas y devuelve el tablero resultante."""
    tablero = iniciar_tablero(n)
    if not resolver_reinas(tablero, 0, n):
        return None  # No hay solución
    return tablero

def mostrar_tablero(tablero):
    """Muestra el tablero en un formato legible."""
    for fila in tablero:
        print(" ".join("Q" if celda == 1 else "." for celda in fila))
