def m_asientos(sala):
    print("\nSala CINE MAYUSCULAS \n actualmente se encuntra así")
    print("  ", end="")
    for col in range(len(sala)):
        print(f"{col+1} ", end="")
    print("\n" + "-" * (len(sala) * 2 + 2))

    for i, fila in enumerate(sala):
        print(f"{i+1}|", end=" ")
        for asiento in fila:
            print(f"{asiento} ", end="")
        print()
    print("--------------------------------\n")

def reservar_asiento(sala, filas, columnas):
    while True:
        try:
            f_sele = int(input(f"Escoge el número de fila (1-{filas}) o puedes pulsar 0 para cancelar: "))
            if f_sele == 0:
                return

            a_sele = int(input(f"Te invitamos a seleccionar un número de asiento (1-{columnas}): "))

            if 1 <= f_sele <= filas and 1 <= a_sele <= columnas:
                _fila = f_sele - 1
                _columna = a_sele - 1

                if sala[_fila][_columna] == 'L':
                    sala[_fila][_columna] = 'X'
                    print(f"Muy bien, el {f_sele}-{a_sele} que elegiste ha sido una reservacion exitosa.\n\n")
                    return
                else:
                    print("Ups!!, Ese asiento ya está ocupado. Tenemos más opciones para elegir.\n")
            else:
                print("Ups!! Lamentamos informarte que has elegido un valor fuera del Rango.\nIntente de nuevo.")
        except ValueError:
            print("Lamentamos decirte que el valor esta fuera de rango. \n Te invitamos a intentarlo de nuevo.")

def liberar_asiento(sala, filas, columnas):
    while True:
        try:
            f_sele = int(input(f"Escoge el número de fila (1-{filas}) o puedes pulsar 0 para cancelar: "))
            if f_sele == 0:
                return

            a_sele = int(input(f"Te invitamos a seleccionar un número de asiento (1-{columnas}): "))

            if 1 <= f_sele <= filas and 1 <= a_sele <= columnas:
                _fila = f_sele - 1
                _columna = a_sele - 1

                if sala[_fila][_columna] == 'X':
                    sala[_fila][_columna] = 'L'
                    print(f"Muy bien, el {f_sele}-{a_sele} que elegiste ha sido liberado exitosamente\n\n")
                    return
                else:
                    print("Ups!! El asiento no puede liberarse porque ya esta disponible.\n Intenta con otro o elegir otra opcion.")
            else:
                print("Lamentamos decirte que el valor esta fuera de rango. \n Te invitamos a intentarlo de nuevo.")
        except ValueError:
            print("Lamentamos decirte que el valor esta fuera de rango. \n Te invitamos a intentarlo de nuevo.")

def contar_asientos(sala):
    libres = 0
    ocupados = 0
    for fila in sala:
        for asiento in fila:
            if asiento == 'L':
                libres += 1
            else:
                ocupados += 1
    print(f"\nCINE MAYUSCULAS conto con ")
    print(f"{libres} asientos libres: ")
    print(f"{ocupados} asientos ocupados")
    print(f"Nuestra sala tiene {libres + ocupados} asientos\n")

def ocupar():
    while True:
        try:
            filas = int(input("Cuantas son las Filas Deseadas en la Sala: "))
            columnas = int(input("Cual es la cantidad de Asientos por cada fila: "))
            break
        except ValueError:
            print("Por favor te invitamos a ingresar un número válido.")

    sala = [['L' for _ in range(columnas)] for _ in range(filas)]

    while True:
        print("\n*********************")
        print("** CINE MAYUSCULAS **")
        print("*********************\n")
        print("Seleccione una opcion de nuestro menú preparado solo para ti")
        print("--------------------------------\n")
        print("1. Mostrar sala")
        print("2. Reservar asiento")
        print("3. Liberar asiento")
        print("4. Contar asientos ocupados y libres")
        print("5. Salir")
        print("--------------------------------\n")
        
        opcion = input("Cual es la eleccion en nuestro menu (1-5): ")

        if opcion == '1':
            m_asientos(sala)
        elif opcion == '2':
            reservar_asiento(sala, filas, columnas)
        elif opcion == '3':
            liberar_asiento(sala, filas, columnas)
        elif opcion == '4':
            contar_asientos(sala)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Lamentamos decirte que el valor esta fuera de rango. \n Te invitamos a intentarlo de nuevo.")

if __name__ == "__main__":
    ocupar()
