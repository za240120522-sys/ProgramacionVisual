import tkinter as tk

def send_command():
    comando = entry.get()
    label_status.config(text=f"Comando enviado: {comando}")

root = tk.Tk()
root.title("Control Electrónico")

entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, padx=5, pady=5)

btn_send = tk.Button(root, text="Enviar", command=send_command)
btn_send.grid(row=0, column=1, padx=5, pady=5)

label_status = tk.Label(root, text="Esperando comando...")
label_status.grid(row=1, column=0, columnspan=2, pady=5)

root.mainloop()




#agrupar botones de no se que 


import tkinter as tk

root = tk.Tk()
root.title("Selección de Modo de Operación")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(pady=10)

tk.Label(frame, text="Selecciona el modo:").pack()

btn_manual = tk.Button(frame, text="Manual")
btn_manual.pack(side="left", padx=5)
btn_auto = tk.Button(frame, text="Automático")
btn_auto.pack(side="left", padx=5)

root.mainloop()