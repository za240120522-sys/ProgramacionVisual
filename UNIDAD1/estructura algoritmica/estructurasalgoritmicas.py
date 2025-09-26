import random
import time

def monitoreo_temperatura():
    print("1. Monitoreo de sensores de temperatura")
    x = [random.randint(50, 100) for _ in range(20)]
    f = False
    i = 0

    while i < len(x):
        t = x[i]
        print(f"Temperatura actual: {t} C")

        if t > 70 and not f:
            print("Ventilador encendido")
            f = True
        else:
            if t < 65 and f:
                print("Ventilador apagado")
                f = False
            else:
                print("Ventilador en funcionamiento")

        if f == True:
            estado_actual = "encendido"
        else:
            estado_actual = "apagado"
        print(f"Estado del ventilador: {estado_actual}")
        i = i + 1
        time.sleep(0.3)
    print("\n--- Fin del monitoreo de temperatura ---\n")


def validacion_clave():
    print("2. Validación de clave de acceso")
    clave_correcta = [1, 2, 3, 4]
    intentos = 0
    max_intentos = 3

    while True:
        if intentos >= max_intentos:
            break
        clave_ingresada = []
        for _ in range(4):
            clave_ingresada.append(random.randint(0, 9))
        print(f"Clave ingresada: {clave_ingresada}")

        coinciden = True
        for idx in range(4):
            if clave_ingresada[idx] != clave_correcta[idx]:
                coinciden = False
                break

        if coinciden == True:
            print("Acceso concedido ")
            break
        else:
            intentos = intentos + 1
            print(f"Clave incorrecta. Intento {intentos} de {max_intentos}")
            if intentos == max_intentos:
                print(" Alarma activada ")

    print("\n--- Fin de validación de clave ---\n")


def adquisicion_voltaje():
    print("3. Adquisición y procesamiento de señales analógicas")
    n = 5
    v = []
    for k in range(n):
        v.append(round(random.uniform(3.0, 4.2), 2))

    contador = 1
    while contador <= len(v):
        valor = v[contador - 1]
        if valor < 3.3:
            mensaje = "Baja"
        else:
            if valor >= 4.0:
                mensaje = "Óptima"
            else:
                mensaje = "Advertencia"
        print(f"Batería {contador}: {valor} V --> {mensaje}")
        contador += 1
    print("\n--- Fin del procesamiento de voltajes ---\n")


def registro_botones():
    print("4. Registro de estados digitales")
    b = []
    for z in range(10):
        b.append(random.choice([True, False]))

    def get_pressed(arr):
        r = []
        for pos in range(len(arr)):
            if arr[pos] == True:
                r.append(pos)
        return r

    print("Estados de los botones (True=presionado, False=no presionado):")
    print(b)
    print("Botones presionados en índices:", get_pressed(b))
    print("\n--- Fin del registro de botones ---\n")


if __name__ == "__main__":
    salir = False
    while salir == False:
        print("1. Monitoreo de sensores de temperatura")
        print("2. Validación de clave de acceso")
        print("3. Adquisición y procesamiento de voltajes")
        print("4. Registro de estados digitales")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            monitoreo_temperatura()
        else:
            if opcion == "2":
                validacion_clave()
            else:
                if opcion == "3":
                    adquisicion_voltaje()
                else:
                    if opcion == "4":
                        registro_botones()
                    else:
                        if opcion == "5":
                            salir = True
                        else:
                            print("Opción inválida, intente de nuevo.")