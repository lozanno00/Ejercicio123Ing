from database import session, HanoiResult

def inicializar_torres(n):
    """Inicializa las torres con los discos."""
    return {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }

def mover_disco(torres, origen, destino):
    """Mueve un disco de una torre a otra."""
    if torres[origen]:
        disco = torres[origen].pop()
        torres[destino].append(disco)

def hanoi_recursivo(n, origen, destino, auxiliar, movimientos):
    """Resuelve el problema de Hanoi de forma recursiva y almacena los movimientos."""
    if n == 1:
        movimientos.append((origen, destino))
        return
    hanoi_recursivo(n - 1, origen, auxiliar, destino, movimientos)
    movimientos.append((origen, destino))
    hanoi_recursivo(n - 1, auxiliar, destino, origen, movimientos)

def calcular_movimientos(n):
    """Calcula todos los movimientos necesarios para resolver el problema."""
    movimientos = []
    hanoi_recursivo(n, 'A', 'C', 'B', movimientos)
    return movimientos

def ejecutar_hanoi_visual(n):
    """Ejecuta el juego de Hanoi y guarda el resultado en la base de datos."""
    torres = inicializar_torres(n)
    movimientos = calcular_movimientos(n)
    print("Estado inicial:")
    mostrar_torres(torres)
    for i, (origen, destino) in enumerate(movimientos, 1):
        print(f"\nMovimiento {i}: Mover disco de {origen} a {destino}")
        mover_disco(torres, origen, destino)
        mostrar_torres(torres)
    print("\nJuego completado.")
    
    estados = "\n".join([f"Estado {i}:\n{estado}" for i, estado in enumerate(visualizar_hanoi(n))])
    
    # Save to database
    resultado = HanoiResult(num_disks=n, result=estados)
    session.add(resultado)
    session.commit()
    
    return estados

def mostrar_torres(torres):
    """Muestra el estado actual de las torres."""
    for torre, discos in torres.items():
        print(f"{torre}: {discos}")
