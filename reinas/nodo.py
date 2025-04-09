class NodoReinas:
    def __init__(self, tablero, fila, padre=None):
        """
        Representa un nodo en el juego de las N Reinas.
        :param tablero: Estado actual del tablero (matriz).
        :param fila: Fila actual donde se está colocando una reina.
        :param padre: Nodo padre (estado anterior).
        """
        self.tablero = tablero
        self.fila = fila
        self.padre = padre

    def __str__(self):
        return f"Fila: {self.fila}, Tablero: {self.tablero}"
