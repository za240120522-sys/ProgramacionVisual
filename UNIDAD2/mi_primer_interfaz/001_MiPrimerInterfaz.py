import tkinter as tk

ventana = tk.Tk()
ventana.title("La GUI más sencilla")
etiqueta = tk.Label(ventana, text="¡Hola gente!")
etiqueta.pack()
ventana.mainloop()
