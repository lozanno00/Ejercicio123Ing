class Caballo:
    
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino

    def __repr__(self):
        return f"Caballo {self.origen}, {self.destino}"
    