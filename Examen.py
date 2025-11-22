def leer_m(filas, columnas):
    matriz = []
    for f in range(filas):
        fila = []
        for c in range(columnas):
            while True:
                try:
                    valor = float(input(f"Ingrese calificación para el estudiante {f+1}, / Materia {c+1}: "))
                    if 0 <= valor <= 100:
                        fila.append(valor)
                        break
                    else:
                        print("Error: Ingrese una calificación entre (0 y 100).")
                except ValueError:
                    print("Error: Ingrese un valor valido.")
        matriz.append(fila)
    return matriz

def imp_m(matriz):
    for fila in matriz:
        print("".join(f"{elem:5.1f}" for elem in fila))

def calcular_promedios_estudiantes(matriz):
    promedios = []
    for fila in matriz:
        promedio = sum(fila) / len(fila)
        promedios.append(promedio)
    return promedios

def calcular_promedios_materias(matriz, columnas):
    promedios = []
    for c in range(columnas):
        suma_columna = 0
        for f in range(len(matriz)):
            suma_columna += matriz[f][c]
        promedios.append(suma_columna / len(matriz))
    return promedios

while True:
    try:
        filas = int(input("Ingresa el número de estudiantes: "))
        columnas = int(input("Ingresa el número de materias: "))
        if filas > 0 and columnas > 0:
            break
        else:
            print("El número de estudiantes y materias debe ser mayor a cero.")
    except ValueError:
        print("Ingrese valores válidos.")

matriz = leer_m(filas, columnas)
maxima_calificacion = matriz[0][0]
minima_calificacion = matriz[0][0]

for f in range(filas):
    for c in range(columnas):
        valor = matriz[f][c]
        if valor > maxima_calificacion:
            maxima_calificacion = valor
        if valor < minima_calificacion:
            minima_calificacion = valor

promedios_estudiantes = calcular_promedios_estudiantes(matriz)
promedios_materias = calcular_promedios_materias(matriz, columnas)

print("\n--- Resultados ---")
print("\nMatriz de Calificaciones:")
imp_m(matriz)
print("\nPromedio de cada estudiante:")
for i, promedio in enumerate(promedios_estudiantes):
    print(f"Estudiante {i+1}: {promedio:.2f}")
print("\nPromedio de cada materia:")
for i, promedio in enumerate(promedios_materias):
    print(f"Materia {i+1}: {promedio:.2f}")
print(f"\nCalificación más alta de la matriz: {maxima_calificacion:.1f}")
print(f"Calificación más baja de la matriz: {minima_calificacion:.1f}")
