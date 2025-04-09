def es_movimiento_valido(x, y, tablero, n):
    """Verifica si el movimiento es válido dentro del tablero."""
    return 0 <= x < n and 0 <= y < n and tablero[x][y] == -1

def resolver_caballo(tablero, x, y, movimiento, movimientos_x, movimientos_y, n):
    """Resuelve el problema del recorrido del caballo usando backtracking."""
    if movimiento == n * n:
        return True

    for i in range(8):
        siguiente_x = x + movimientos_x[i]
        siguiente_y = y + movimientos_y[i]
        if es_movimiento_valido(siguiente_x, siguiente_y, tablero, n):
            tablero[siguiente_x][siguiente_y] = movimiento
            if resolver_caballo(tablero, siguiente_x, siguiente_y, movimiento + 1, movimientos_x, movimientos_y, n):
                return True
            tablero[siguiente_x][siguiente_y] = -1  # Backtracking

    return False

def iniciar_tablero(n):
    """Inicializa el tablero con -1."""
    return [[-1 for _ in range(n)] for _ in range(n)]

def recorrido_caballo(n):
    """Inicia el recorrido del caballo."""
    tablero = iniciar_tablero(n)
    movimientos_x = [2, 1, -1, -2, -2, -1, 1, 2]
    movimientos_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Posición inicial del caballo
    tablero[0][0] = 0

    if not resolver_caballo(tablero, 0, 0, 1, movimientos_x, movimientos_y, n):
        return None  # No hay solución
    return tablero

def mostrar_tablero(tablero):
    """Muestra el tablero en un formato legible."""
    for fila in tablero:
        print(" ".join(f"{celda:2}" for celda in fila))

def ejecutar_caballo():
    """Ejecuta el juego del recorrido del caballo."""
    print("Juego del recorrido del caballo")
    n = int(input("Ingrese el tamaño del tablero (n x n): "))
    tablero = recorrido_caballo(n)
    if tablero:
        print("Recorrido completado:")
        mostrar_tablero(tablero)
    else:
        print("No se encontró una solución para el tamaño del tablero proporcionado.")
