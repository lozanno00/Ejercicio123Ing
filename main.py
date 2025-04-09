import tkinter as tk
from tkinter import ttk, scrolledtext, Canvas
from hanoi.juego import calcular_movimientos, inicializar_torres
from Caballo.caballo import ejecutar_caballo
from reinas.juego import ejecutar_reinas

def ejecutar_hanoi_tk(n, output_widget, canvas):
    """Ejecuta el juego de Hanoi y muestra los estados en el widget de salida y gráficamente."""
    torres = inicializar_torres(n)
    movimientos = calcular_movimientos(n)
    output_widget.delete(1.0, tk.END)
    output_widget.insert(tk.END, "Estado inicial:\n")
    output_widget.insert(tk.END, mostrar_torres_tk(torres) + "\n")
    dibujar_torres(canvas, torres, n)

    for i, (origen, destino) in enumerate(movimientos, 1):
        torres[destino].append(torres[origen].pop())
        output_widget.insert(tk.END, f"Movimiento {i}: Mover de {origen} a {destino}\n")
        output_widget.insert(tk.END, mostrar_torres_tk(torres) + "\n")
        dibujar_torres(canvas, torres, n)
        canvas.update()
        canvas.after(500)  # Delay for animation

def mostrar_torres_tk(torres):
    """Devuelve una representación en texto del estado actual de las torres."""
    resultado = []
    for torre, discos in torres.items():
        resultado.append(f"{torre}: {' '.join(map(str, discos)) if discos else 'Vacío'}")
    return "\n".join(resultado)

def dibujar_torres(canvas, torres, n):
    """Dibuja las torres y los discos en el canvas."""
    canvas.delete("all")
    ancho_canvas = 600
    alto_canvas = 400
    ancho_torre = ancho_canvas // 3
    alto_base = 20
    ancho_disco_max = ancho_torre - 40
    alto_disco = 20

    # Dibujar las bases de las torres
    for i in range(3):
        x1 = i * ancho_torre + 20
        x2 = (i + 1) * ancho_torre - 20
        y1 = alto_canvas - alto_base
        y2 = alto_canvas
        canvas.create_rectangle(x1, y1, x2, y2, fill="black")

    # Dibujar los discos
    for i, torre in enumerate(["A", "B", "C"]):
        x_centro = i * ancho_torre + ancho_torre // 2
        y_base = alto_canvas - alto_base
        for j, disco in enumerate(reversed(torres[torre])):
            ancho_disco = ancho_disco_max * disco // n
            x1 = x_centro - ancho_disco // 2
            x2 = x_centro + ancho_disco // 2
            y1 = y_base - (j + 1) * alto_disco
            y2 = y_base - j * alto_disco
            canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")

def ejecutar_caballo_tk(n, output_widget):
    """Ejecuta el recorrido del caballo y muestra el tablero en el widget de salida."""
    resultado = ejecutar_caballo(n)
    output_widget.delete(1.0, tk.END)
    output_widget.insert(tk.END, resultado)

def ejecutar_reinas_tk(n, output_widget, canvas):
    """Ejecuta el juego de las N Reinas y muestra el tablero en el widget de salida y gráficamente."""
    resultado = ejecutar_reinas(n)
    output_widget.delete(1.0, tk.END)
    if "No se encontró una solución" in resultado:
        output_widget.insert(tk.END, resultado)
        return

    # Mostrar el resultado en texto
    output_widget.insert(tk.END, resultado)

    # Representar gráficamente el tablero
    canvas.delete("all")
    cell_size = 500 // n  # Ajustar el tamaño de las celdas según el tamaño del tablero
    tablero = [[1 if c == "Q" else 0 for c in row.split()] for row in resultado.split("\n") if row]

    for i in range(n):
        for j in range(n):
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            color = "white" if (i + j) % 2 == 0 else "gray"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
            if tablero[i][j] == 1:
                canvas.create_oval(
                    x1 + cell_size // 4,
                    y1 + cell_size // 4,
                    x2 - cell_size // 4,
                    y2 - cell_size // 4,
                    fill="black"
                )

def main():
    root = tk.Tk()
    root.title("Juegos Visuales: Torres de Hanoi, Recorrido del Caballo, N Reinas")

    # Tabs
    tab_control = ttk.Notebook(root)
    tab_hanoi = ttk.Frame(tab_control)
    tab_caballo = ttk.Frame(tab_control)
    tab_reinas = ttk.Frame(tab_control)
    tab_control.add(tab_hanoi, text="Torres de Hanoi")
    tab_control.add(tab_caballo, text="Recorrido del Caballo")
    tab_control.add(tab_reinas, text="N Reinas")
    tab_control.pack(expand=1, fill="both")

    # Torres de Hanoi
    ttk.Label(tab_hanoi, text="Número de discos:").pack(pady=5)
    hanoi_input = ttk.Entry(tab_hanoi)
    hanoi_input.pack(pady=5)
    hanoi_output = scrolledtext.ScrolledText(tab_hanoi, width=50, height=10)
    hanoi_output.pack(pady=5)
    hanoi_canvas = Canvas(tab_hanoi, width=600, height=400, bg="white")
    hanoi_canvas.pack(pady=5)
    ttk.Button(
        tab_hanoi,
        text="Ejecutar",
        command=lambda: ejecutar_hanoi_tk(int(hanoi_input.get()), hanoi_output, hanoi_canvas)
    ).pack(pady=5)

    # Recorrido del Caballo
    ttk.Label(tab_caballo, text="Tamaño del tablero (n x n):").pack(pady=5)
    caballo_input = ttk.Entry(tab_caballo)
    caballo_input.pack(pady=5)
    caballo_output = scrolledtext.ScrolledText(tab_caballo, width=50, height=10)
    caballo_output.pack(pady=5)
    ttk.Button(
        tab_caballo,
        text="Ejecutar",
        command=lambda: ejecutar_caballo_tk(int(caballo_input.get()), caballo_output)
    ).pack(pady=5)

    # N Reinas
    ttk.Label(tab_reinas, text="Tamaño del tablero (n x n):").pack(pady=5)
    reinas_input = ttk.Entry(tab_reinas)
    reinas_input.pack(pady=5)
    reinas_output = scrolledtext.ScrolledText(tab_reinas, width=50, height=10)
    reinas_output.pack(pady=5)
    reinas_canvas = Canvas(tab_reinas, width=500, height=500, bg="white")
    reinas_canvas.pack(pady=5)
    ttk.Button(
        tab_reinas,
        text="Ejecutar",
        command=lambda: ejecutar_reinas_tk(int(reinas_input.get()), reinas_output, reinas_canvas)
    ).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
