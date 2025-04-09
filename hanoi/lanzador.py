import tkinter as tk
from tkinter import ttk, scrolledtext
from hanoi.juego import calcular_movimientos, inicializar_torres  # Use absolute import

def ejecutar_hanoi_tk(n, output_widget):
    """Ejecuta el juego de Hanoi y muestra los estados en el widget de salida."""
    torres = inicializar_torres(n)
    movimientos = calcular_movimientos(n)
    output_widget.delete(1.0, tk.END)
    output_widget.insert(tk.END, "Estado inicial:\n")
    output_widget.insert(tk.END, mostrar_torres_tk(torres) + "\n")
    for i, (origen, destino) in enumerate(movimientos, 1):
        torres[destino].append(torres[origen].pop())
        output_widget.insert(tk.END, f"Movimiento {i}: Mover de {origen} a {destino}\n")
        output_widget.insert(tk.END, mostrar_torres_tk(torres) + "\n")

def mostrar_torres_tk(torres):
    """Devuelve una representación en texto del estado actual de las torres."""
    resultado = []
    for torre, discos in torres.items():
        resultado.append(f"{torre}: {' '.join(map(str, discos)) if discos else 'Vacío'}")
    return "\n".join(resultado)

def main():
    root = tk.Tk()
    root.title("Torres de Hanoi - Visualización")

    ttk.Label(root, text="Número de discos:").pack(pady=5)
    hanoi_input = ttk.Entry(root)
    hanoi_input.pack(pady=5)

    hanoi_output = scrolledtext.ScrolledText(root, width=50, height=20)
    hanoi_output.pack(pady=5)

    ttk.Button(
        root,
        text="Ejecutar",
        command=lambda: ejecutar_hanoi_tk(int(hanoi_input.get()), hanoi_output)
    ).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()

