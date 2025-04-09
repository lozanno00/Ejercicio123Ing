import tkinter as tk
from tkinter import ttk, scrolledtext
from reinas.juego import n_reinas

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
    root.title("N Reinas - Visualización")

    ttk.Label(root, text="Tamaño del tablero (n x n):").pack(pady=5)
    reinas_input = ttk.Entry(root)
    reinas_input.pack(pady=5)

    reinas_output = scrolledtext.ScrolledText(root, width=50, height=20)
    reinas_output.pack(pady=5)

    ttk.Button(
        root,
        text="Ejecutar",
        command=lambda: ejecutar_reinas_tk(int(reinas_input.get()), reinas_output)
    ).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
