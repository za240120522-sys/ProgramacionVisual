import tkinter as tk

def enviar():
    valor = entry.get()
    if valor.isdigit():
        label_estado.config(text=f"Valor almacenado: {valor}")
    else:
        label_estado.config(text="Solo números permitidos")

root = tk.Tk()
root.title("Entrada y validación de datos")

entry = tk.Entry(root)
entry.grid(row=0, column=0, padx=5, pady=5)
boton = tk.Button(root, text="Enviar", command=enviar)
boton.grid(row=0, column=1, padx=5, pady=5)

label_estado = tk.Label(root, text="Esperando datos...")
label_estado.grid(row=1, column=0, columnspan=2)

root.mainloop()



import tkinter as tk

def seleccionar_canal():
    canal = spin.get()
    label.set(f"Canal digital seleccionado: {canal}")

root = tk.Tk()
root.title("Configuración de canal")

spin = tk.Spinbox(root, from_=1, to=8)
spin.pack(pady=5)
tk.Button(root, text="Seleccionar", command=seleccionar_canal).pack()
label = tk.StringVar()
tk.Label(root, textvariable=label).pack(pady=5)

root.mainloop()



import tkinter as tk
from tkinter import ttk

def elegir_sensor(event=None):
    seleccion = combo.get()
    etiqueta.set(f"Tipo de sensor: {seleccion}")

root = tk.Tk()
root.title("Selección de sensor")

lista = ["Temperatura", "Luminosidad", "Humedad", "Movimiento","eeee"]
combo = ttk.Combobox(root, values=lista, state="readonly")
combo.pack(pady=5)
combo.bind("<<ComboboxSelected>>", elegir_sensor)
etiqueta = tk.StringVar()
ttk.Label(root, textvariable=etiqueta).pack(pady=5)

root.mainloop()


import tkinter as tk
from tkinter import messagebox

def guardar():
    messagebox.showinfo("Configuración", "La configuración se guardó correctamente.")

root = tk.Tk()
root.title("Formulario IoT")
tk.Button(root, text="Guardar", command=guardar).pack(pady=20)

root.mainloop()




import tkinter as tk

def solo_numeros(P):
    return P.isdigit()

root = tk.Tk()
root.title("Validación en tiempo real")

vcmd = (root.register(solo_numeros), "%P")
entry = tk.Entry(root, validate="key", validatecommand=vcmd)
entry.pack(padx=10, pady=10)

root.mainloop()