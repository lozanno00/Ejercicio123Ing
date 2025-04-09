class NodoHanoi:
    def __init__(self, torres, movimiento=None, padre=None):
        """
        Representa un nodo en el juego de las Torres de Hanoi.
        :param torres: Estado actual de las torres (diccionario).
        :param movimiento: Movimiento realizado para llegar a este estado.
        :param padre: Nodo padre (estado anterior).
        """
        self.torres = torres
        self.movimiento = movimiento
        self.padre = padre

    def __str__(self):
        return f"Movimiento: {self.movimiento}, Torres: {self.torres}"