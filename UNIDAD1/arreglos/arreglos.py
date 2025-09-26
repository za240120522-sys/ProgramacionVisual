import random
import time

# 1. Monitoreo de sensores de temperatura
def monitoreo_temperatura():
    print("\n## 1. Monitoreo de sensores de temperatura ##")
    lecturas_temp = [random.randint(52, 102) for _ in range(22)]  # ligera variación en rango y cantidad
    ventilador_activo = False
    idx = 0

    while idx < len(lecturas_temp):
        temp_actual = lecturas_temp[idx]
        print(f"Temperatura actual: {temp_actual} °C")

        if temp_actual > 72 and not ventilador_activo:
            print("Ventilador encendido")
            ventilador_activo = True
        elif temp_actual < 63 and ventilador_activo:
            print("Ventilador apagado")
            ventilador_activo = False
        else:
            print("Ventilador en funcionamiento")

        estado_vent = "encendido" if ventilador_activo else "apagado"
        print(f"Estado del ventilador: {estado_vent}")
        idx += 1
        time.sleep(0.28)  # ligera reducción del retraso
    print("\n--- Fin del monitoreo de temperatura ---\n")


# 2. Validación de clave de acceso
def validacion_clave():
    print("\n## 2. Validación de clave de acceso ##")
    clave_valida = [2, 3, 4, 5]  # clave ligeramente cambiada
    intentos_realizados = 0
    max_intentos = 4  # aumentado a 4 intentos

    while intentos_realizados < max_intentos:
        clave_propuesta = [random.randint(0, 9) for _ in range(4)]  # simulación
        print(f"Clave ingresada: {clave_propuesta}")

        if clave_propuesta == clave_valida:
            print("Acceso concedido")
            break
        else:
            intentos_realizados += 1
            print(f"Clave incorrecta. Intento {intentos_realizados} de {max_intentos}")

        if intentos_realizados == max_intentos:
            print(" ¡Alarma activada! ¡Alerta! ")
    print("\n--- Fin de validación de clave ---\n")


# 3. Adquisición y procesamiento de señales analógicas
def adquisicion_voltaje():
    print("\n## 3. Adquisición y procesamiento de señales analógicas ##")
    num_dispositivos = 6  # aumentado a 6 dispositivos
    niveles_voltaje = [round(random.uniform(2.9, 4.3), 2) for _ in range(num_dispositivos)]

    for num, voltaje in enumerate(niveles_voltaje, 1):
        if voltaje < 3.2:
            print(f"Batería {num}: {voltaje} V --> Baja ")
        elif voltaje >= 4.1:
            print(f"Batería {num}: {voltaje} V --> Óptima ")
        else:
            print(f"Batería {num}: {voltaje} V --> Advertencia ")
    print("\n--- Fin del procesamiento de voltajes ---\n")


# 4. Registro de estados digitales
def registro_botones():
    print("\n## 4. Registro de estados digitales ##")
    estados_botones = [random.choice([True, False]) for _ in range(12)]  # ahora 12 botones

    def obtener_presionados(estados):
        """Devuelve los índices de los botones presionados"""
        return [i for i, estado in enumerate(estados) if estado]

    print("Estados de los botones (True=presionado, False=no presionado):")
    print(estados_botones)
    print("Botones presionados en índices:", obtener_presionados(estados_botones))
    print("\n--- Fin del registro de botones ---\n")


# Menú principal
if __name__ == "__main__":
    while True:
        print("1. Monitoreo de sensores de temperatura")
        print("2. Validar clave de acceso")
        print("3. Adquisición y procesamiento de voltajes")
        print("4. Registro de estados digitales")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            monitoreo_temperatura()
        elif opcion == "2":
            validacion_clave()
        elif opcion == "3":
            adquisicion_voltaje()
        elif opcion == "4":
            registro_botones()
        elif opcion == "5":
            print("Programa finalizado")
            break
        else:
            print("Opción inválida, intente de nuevo.")