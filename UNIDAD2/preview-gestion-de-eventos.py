#1. Asociando funciones a botones – parámetro command

import tkinter as tk

def encender_led():
    label_estado.config(text="LED encendido")

root = tk.Tk()
root.title("Panel de control electrónico")

label_estado = tk.Label(root, text="LED apagado")
label_estado.pack(pady=10)

btn_encender = tk.Button(root, text="Encender LED", command=encender_led)
btn_encender.pack(pady=5)

root.mainloop()


#2. Uso de StringVar e IntVar para entrada/salida
import tkinter as tk

def actualizar_temperatura():
    valor = entrada_temp.get()
    etiqueta_temp.set(f"Temperatura registrada: {valor} °C")

root = tk.Tk()
root.title("Monitor de temperatura")

etiqueta_temp = tk.StringVar()
etiqueta_temp.set("Temperatura registrada: -- °C")

tk.Label(root, textvariable=etiqueta_temp).pack(pady=10)
entrada_temp = tk.Entry(root)
entrada_temp.pack(pady=5)
tk.Button(root, text="Actualizar", command=actualizar_temperatura).pack()


root.mainloop()


#3. Captura de eventos personalizados (bind)

import tkinter as tk

def mostrar_coordenadas(event):
    mensaje.set(f"Coordenadas del clic: x={event.x}, y={event.y}")

root = tk.Tk()
root.title("Lectura de clic en pantalla")

mensaje = tk.StringVar()
tk.Label(root, textvariable=mensaje, font=("Arial", 14)).pack(pady=10)

panel = tk.Frame(root, width=200, height=100, bg="#e0f2f1")
panel.pack(pady=10)
panel.bind("<Button-1>", mostrar_coordenadas)  # Captura clic izquierdo

root.mainloop()



#validaciones

import tkinter as tk

def validar_numero(*args):
    valor = v_numero.get()
    if not valor.isdigit():
        estado.set("Solo números permitidos")
    else:
        estado.set("Valor válido")

root = tk.Tk()
root.title("Validación de entrada numérica")

v_numero = tk.StringVar()
v_numero.trace("w", validar_numero)  

tk.Entry(root, textvariable=v_numero).pack(pady=5)
estado = tk.StringVar(value="Esperando entrada...")
tk.Label(root, textvariable=estado).pack()

root.mainloop()




