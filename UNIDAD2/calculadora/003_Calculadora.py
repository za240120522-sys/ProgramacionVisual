import tkinter as tk

def presionar(valor):
    entry.insert(tk.END, valor)

def calcular():
    try:
        expresion = entry.get()
        if len(expresion) > 0:
            resultado = eval(expresion)
            label_resultado.config(text=f"= {resultado}")
        else:
            label_resultado.config(text="= ")
    except Exception:
        label_resultado.config(text="Error")

def borrar():
    if entry.get() != "":
        entry.delete(0, tk.END)
    label_resultado.config(text="= ")

ventana = tk.Tk()
ventana.title("Calculadora con Texto Blanco")

# Etiqueta de entrada
label_entrada = tk.Label(ventana, text="Entrada:")
label_entrada.grid(row=0, column=0, padx=5, pady=5)

# ✅ ENTRY con texto blanco, fondo negro y cursor blanco
entry = tk.Entry(ventana, width=35, fg="white", bg="black", insertbackground="white")
entry.grid(row=0, column=1, columnspan=4, padx=5, pady=5)

# Botones manuales

# Fila 1
tk.Button(ventana, text="1", width=5, height=2, command=lambda: presionar("1")).grid(row=1, column=0)
tk.Button(ventana, text="2", width=5, height=2, command=lambda: presionar("2")).grid(row=1, column=1)
tk.Button(ventana, text="3", width=5, height=2, command=lambda: presionar("3")).grid(row=1, column=2)
tk.Button(ventana, text="+", width=5, height=2, command=lambda: presionar("+")).grid(row=1, column=3)

# Fila 2
tk.Button(ventana, text="4", width=5, height=2, command=lambda: presionar("4")).grid(row=2, column=0)
tk.Button(ventana, text="5", width=5, height=2, command=lambda: presionar("5")).grid(row=2, column=1)
tk.Button(ventana, text="6", width=5, height=2, command=lambda: presionar("6")).grid(row=2, column=2)
tk.Button(ventana, text="-", width=5, height=2, command=lambda: presionar("-")).grid(row=2, column=3)

# Fila 3
tk.Button(ventana, text="7", width=5, height=2, command=lambda: presionar("7")).grid(row=3, column=0)
tk.Button(ventana, text="8", width=5, height=2, command=lambda: presionar("8")).grid(row=3, column=1)
tk.Button(ventana, text="9", width=5, height=2, command=lambda: presionar("9")).grid(row=3, column=2)
tk.Button(ventana, text="*", width=5, height=2, command=lambda: presionar("*")).grid(row=3, column=3)

# Fila 4
tk.Button(ventana, text="0", width=5, height=2, command=lambda: presionar("0")).grid(row=4, column=0)
tk.Button(ventana, text="C", width=5, height=2, command=borrar).grid(row=4, column=1)
tk.Button(ventana, text="=", width=5, height=2, command=calcular).grid(row=4, column=2)
tk.Button(ventana, text="/", width=5, height=2, command=lambda: presionar("/")).grid(row=4, column=3)

# Resultado
label_resultado = tk.Label(ventana, text="= ")
label_resultado.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

ventana.mainloop()
