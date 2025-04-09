class NodoCaballo:
    def __init__(self, tablero, posicion, movimiento=None, padre=None):
        """
        Representa un nodo en el juego del recorrido del Caballo.
        :param tablero: Estado actual del tablero (matriz).
        :param posicion: Posición actual del caballo (x, y).
        :param movimiento: Movimiento realizado para llegar a este estado.
        :param padre: Nodo padre (estado anterior).
        """
        self.tablero = tablero
        self.posicion = posicion
        self.movimiento = movimiento
        self.padre = padre

    def __str__(self):
        return f"Movimiento: {self.movimiento}, Posición: {self.posicion}, Tablero: {self.tablero}"
