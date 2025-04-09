import tkinter as tk
from tkinter import ttk, scrolledtext
from Caballo.caballo import recorrido_caballo

def ejecutar_caballo_tk(n, output_widget):
    """Ejecuta el recorrido del caballo y muestra el tablero en el widget de salida."""
    tablero = recorrido_caballo(n)
    output_widget.delete(1.0, tk.END)
    if tablero:
        output_widget.insert(tk.END, "\n".join([" ".join(f"{celda:2}" for celda in fila) for fila in tablero]))
    else:
        output_widget.insert(tk.END, "No se encontró una solución.")

def main():
    root = tk.Tk()
    root.title("Recorrido del Caballo - Visualización")

    ttk.Label(root, text="Tamaño del tablero (n x n):").pack(pady=5)
    caballo_input = ttk.Entry(root)
    caballo_input.pack(pady=5)

    caballo_output = scrolledtext.ScrolledText(root, width=50, height=20)
    caballo_output.pack(pady=5)

    ttk.Button(
        root,
        text="Ejecutar",
        command=lambda: ejecutar_caballo_tk(int(caballo_input.get()), caballo_output)
    ).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
