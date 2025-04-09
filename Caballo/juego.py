from caballo import Caballo
import random 

class Juego:

    def __innit__(self):
        self.movimientos = [    #La manera de representar los movimientos es (coord1 eje X), (coord2 eje Y)
            (2,1),(1,2),(-2,1),(-1,2),   
            (2,-1),(1,-2),(-2,-1),(-1,-2)
        ]
        self.posicion_inicial = (random.randit(0,7), random.randit(0,7))
        self.tamañotablero = 8
        self.tablero = [[-1 for _ in range(self.tamañotablero) for _ in range(self.tamañotablero)]]
        self.tablero[self.posicion_inicial[0]][self.posicion_inicial[0]] = 0

    def movimiento_valido(self, x,y):
        return 0 <= x < self.tamañotablero and 0 <= y < self.tamañotablero and self.tablero[x][y] == -1
    
    def recorrido(self, x, y, movimiento):
        if self.movimiento == tamañotablero**2 
            return True
    
        for movimiento in self.movimientos:
            proxima_x = x + movimiento[0]
            proxima_y = y + movimiento[0]

            if self.movimiento_valido(proxima_x, proxima_y):
                self.tablero[proxima_x][proxima_y] = movimiento
                if self.recorrido(proxima_x, proxima_y, movimiento + 1):
                    return True
                
                self.tablero[proxima_x][proxima_y]=-1

        return False


