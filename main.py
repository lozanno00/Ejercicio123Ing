import tkinter as tk
from tkinter import ttk, scrolledtext
from hanoi.juego import ejecutar_hanoi_visual, calcular_movimientos, inicializar_torres
from Caballo.caballo import recorrido_caballo
from reinas.juego import n_reinas

def ejecutar_hanoi_tk(n, output_widget):
    """Ejecuta el juego de Hanoi y muestra los estados en el widget de salida."""
    estados = ejecutar_hanoi_visual(n)
    output_widget.delete(1.0, tk.END)
    output_widget.insert(tk.END, estados)

def ejecutar_caballo_tk(n, output_widget):
    """Ejecuta el recorrido del caballo y muestra el tablero en el widget de salida."""
    tablero = recorrido_caballo(n)
    output_widget.delete(1.0, tk.END)
    if tablero:
        output_widget.insert(tk.END, "\n".join([" ".join(f"{celda:2}" for celda in fila) for fila in tablero]))
    else:
        output_widget.insert(tk.END, "No se encontró una solución.")

def ejecutar_reinas_tk(n, output_widget):
    """Ejecuta el juego de las N Reinas y muestra el tablero en el widget de salida."""
    tablero = n_reinas(n)
    output_widget.delete(1.0, tk.END)
    if tablero:
        output_widget.insert(tk.END, "\n".join([" ".join("Q" if celda == 1 else "." for celda in fila) for fila in tablero]))
    else:
        output_widget.insert(tk.END, "No se encontró una solución.")

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
    hanoi_output = scrolledtext.ScrolledText(tab_hanoi, width=50, height=20)
    hanoi_output.pack(pady=5)
    ttk.Button(tab_hanoi, text="Ejecutar", command=lambda: ejecutar_hanoi_tk(int(hanoi_input.get()), hanoi_output)).pack(pady=5)

    # Recorrido del Caballo
    ttk.Label(tab_caballo, text="Tamaño del tablero (n x n):").pack(pady=5)
    caballo_input = ttk.Entry(tab_caballo)
    caballo_input.pack(pady=5)
    caballo_output = scrolledtext.ScrolledText(tab_caballo, width=50, height=20)
    caballo_output.pack(pady=5)
    ttk.Button(tab_caballo, text="Ejecutar", command=lambda: ejecutar_caballo_tk(int(caballo_input.get()), caballo_output)).pack(pady=5)

    # N Reinas
    ttk.Label(tab_reinas, text="Tamaño del tablero (n x n):").pack(pady=5)
    reinas_input = ttk.Entry(tab_reinas)
    reinas_input.pack(pady=5)
    reinas_output = scrolledtext.ScrolledText(tab_reinas, width=50, height=20)
    reinas_output.pack(pady=5)
    ttk.Button(tab_reinas, text="Ejecutar", command=lambda: ejecutar_reinas_tk(int(reinas_input.get()), reinas_output)).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
