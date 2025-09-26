def problema1():
    # Registro de consumo eléctrico por electrodoméstico
    consumos = {
        "refri": 50,
        "lavadora": 30,
        "tv": 20,
        "horno": 80,
        "aire acondicionado": 80
    }

    total = 0
    for consumo in consumos.values():
        total += consumo

    print("1. Consumo total:", total, "kWh")
    print("Porcentajes por electrodoméstico:")

    for electro, consumo in consumos.items():
        porcentaje = (consumo / total) * 100
        print(electro, ":", round(porcentaje, 2), "%")
        if porcentaje > 30:
            print("  --> Este electrodoméstico supera el 30%")


def problema2():
   
    averias = [
        ("2024-04-01", "cortocircuito"),
        ("2024-04-02", "fusible quemado"),
        ("2024-04-03", "cortocircuito"),
        ("2024-04-04", "sobrecarga"),
        ("2024-04-05", "cortocircuito")
    ]

    conteo = {}
    for fecha, tipo in averias:
        if tipo in conteo:
            conteo[tipo] += 1
        else:
            conteo[tipo] = 1

    print("2. Cantidad de cada tipo de avería:")
    for tipo, cantidad in conteo.items():
        print(tipo, ":", cantidad)

    mas_frecuente = ""
    max_veces = 0
    for tipo, cantidad in conteo.items():
        if cantidad > max_veces:
            max_veces = cantidad
            mas_frecuente = tipo

    print("Avería más frecuente:", mas_frecuente)


def problema3():
    
    señales = []
    contador = 0

    while True:
        señal = input("Ingresa una señal (0 o 1): ")
        if señal == "0" or señal == "1":
            señales.append(señal)
            contador += 1
        else:
            print("Señal inválida. Ingresa 0 o 1.")
        
        if contador == 20:
            break

    altas = 0
    bajas = 0
    for s in señales:
        if s == "1":
            altas += 1
        else:
            bajas += 1

    print("3. Señales altas (1):", altas)
    print("Señales bajas (0):", bajas)

    if altas > bajas:
        print("Indicador activado: más señales altas que bajas.")
    else:
        print("Indicador no activado.")


def problema4():
    
    estados = ["apto", "correcto", "reparar", "apto", "reparar", "reparar", "correcto"]

    reparaciones = 0
    for estado in estados:
        if estado == "reparar":
            reparaciones += 1

    print("4. Departamentos que requieren reparación:", reparaciones)

    if reparaciones > 2:
        print("Alerta: hay más de 2 reparaciones necesarias.")


def problema5():
    # Listado único de suministros eléctricos
    proyecto1 = ["cable", "interruptor", "toma corriente", "cable"]
    proyecto2 = ["fusible", "interruptor", "cable", "regleta"]
    proyecto3 = ["toma corriente", "regleta", "fusible"]

    todos = proyecto1 + proyecto2 + proyecto3
    unicos = set(todos)

    print("5. Suministros únicos:")
    for item in unicos:
        print(item)


def problema6():
   
    interrupciones = [
        ("08:00", "08:30"),
        ("12:15", "12:45"),
        ("18:00", "19:00")
    ]

    total_minutos = 0
    for inicio, fin in interrupciones:
        h1, m1 = map(int, inicio.split(":"))
        h2, m2 = map(int, fin.split(":"))
        minutos_inicio = h1 * 60 + m1
        minutos_fin = h2 * 60 + m2
        duracion = minutos_fin - minutos_inicio
        total_minutos += duracion

    print("6. Tiempo total sin energía:", total_minutos, "minutos")

    if total_minutos > 60:
        print("Alerta: más de 1 hora sin energía.")


def problema7():
   
    fechas = set()

    while True:
        fecha = input("Ingresa una fecha para mantenimiento (YYYY-MM-DD) o 'fin' para terminar: ")
        if fecha == "fin":
            break
        fechas.add(fecha)

    agenda_ordenada = sorted(fechas)
    print("7. Agenda de mantenimientos:")
    for f in agenda_ordenada:
        print(f)


def problema8():
   
    habitaciones = {
        "sala": [100, 60, 50],
        "cocina": [1500, 800, 200],
        "dormitorio": [40, 60, 10]
    }

    total_general = 0
    print("8. Potencia por habitación:")

    for habitacion, potencias in habitaciones.items():
        total_hab = sum(potencias)
        total_general += total_hab
        print(habitacion, ":", total_hab, "W")
        if total_hab > 1000:
            print("  --> Esta habitación supera el límite de 1000W")

    print("Potencia total general:", total_general, "W")


def problema9():
    
    incidencias = {
        "2024-04-01": 1,
        "2024-04-02": 3,
        "2024-04-03": 1,
        "2024-04-04": 2,
        "2024-04-05": 1
    }

    print("9. Días con más de una fuga:")
    for fecha, cantidad in incidencias.items():
        if cantidad > 1:
            print(fecha, ":", cantidad, "fugas")


def problema10():
   
    cargas = [2000, 1500, 1800, 2200, 1600, 1900]

    fase1 = []
    fase2 = []
    fase3 = []

    for i, carga in enumerate(cargas):
        if i % 3 == 0:
            fase1.append(carga)
        elif i % 3 == 1:
            fase2.append(carga)
        else:
            fase3.append(carga)

    fases = [fase1, fase2, fase3]
    limite = 4000

    print("10. Carga por fase:")
    for i, fase in enumerate(fases):
        total_fase = sum(fase)
        print("Fase", i+1, ":", total_fase, "W")
        if total_fase > limite:
            print("  --> Fase", i+1, "sobrecargada")


if __name__ == "__main__":
    while True:  
        print("\nElige un problema para ejecutar (1 al 10) o 0 para salir:")
        try:
            opcion = int(input("Número del problema: "))
            
            if opcion == 0:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            elif opcion == 1:
                problema1()
            elif opcion == 2:
                problema2()
            elif opcion == 3:
                problema3()
            elif opcion == 4:
                problema4()
            elif opcion == 5:
                problema5()
            elif opcion == 6:
                problema6()
            elif opcion == 7:
                problema7()
            elif opcion == 8:
                problema8()
            elif opcion == 9:
                problema9()
            elif opcion == 10:
                problema10()
            else:
                print("Opción no válida. Elige un número entre 0 y 10.")
                
        except ValueError:
            print("Por favor, ingresa un número válido.")