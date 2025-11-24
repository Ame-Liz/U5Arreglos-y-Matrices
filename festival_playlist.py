nm = []
art = []
drc = []
plrs = []

def menu():
    print("\nEy Hola!, Que opcion te gustaria tomar (1-5)")
    print("--------------------------------\n")
    print("1. Agregar canciones")
    print("2. Ver reportes")
    print("3. Buscar canciones (Filtrar)")
    print("4. Playlist recomendada (Bonus)")
    print("5. Salir")

def agg_c():
    while True:
        try:
            cantidad = int(input("¿Cuántas canciones Deaseas agragar?"))
            if cantidad <= 0:
                print("Ooh-oh!, Debes agregar al menos una canción.")
                continue
            break
        except ValueError:
            print("Debes agregar datos validos, Intenta de nuevo.")
            
    for i in range(cantidad):
        print(f"\n--- Canción {len(nm) + 1} ---")
        nombre_input = input("Nombre de la canción: ").strip().title()
        artista_input = input("Artista: ").strip().title()
        
        while True:
            try:
                duracion_input_val = float(input("Duración (min) : "))
                if duracion_input_val <= 0:
                    print("Ooh-oh!, No es valido tu valor. Intenta de nuevo.")
                    continue
                break
            except ValueError:
                print("Ingrese una duración válida.")
                
        while True:
            try:
                popularidad_input = int(input("Popularidad (1-100): "))
                if 1 <= popularidad_input <= 100:
                    break
                else:
                    print("Ooh-oh!, La popularidad debe estar son rango entre 1 y 100.")
            except ValueError:
                print("Ingrese un número valido")
        
        nm.append(nombre_input)
        art.append(artista_input)
        drc.append(duracion_input_val)
        plrs.append(popularidad_input)
        print("--------------------------------\n")
        print(f"Canción '{nombre_input}' agregada con éxito.")

def rpts():
    if not nm:
        print("No hay canciones registradas para realizar esta funcion")
        return
        
    tot_c = len(nm)
    duracion = sum(drc)
    prom = sum(plrs) / tot_c
    
    ind_mas = plrs.index(max(plrs))
    ind_menos = plrs.index(min(plrs))
    
    cc_mas = nm[ind_mas]
    art_mas = art[ind_mas]
    
    cc_menos = nm[ind_menos]
    art_menos = art[ind_menos]

    print("--------------------------------\n")
    print("\n Playlist ")
    print("--------------------------------\n")
    print(f"Número total de canciones: {tot_c}")
    print(f"Duración total de la playlist: {duracion:.2f} min")
    print(f"Canción más popular: '{cc_mas}' de {art_mas} ({max(plrs)}/100)")
    print(f"Canción menos popular: '{cc_menos}' de {art_menos} ({min(plrs)}/100)")
    print(f"Promedio de popularidad: {prom:.2f}/100")

def filtro():
    if not nm:
        print("Ooh-oh!, Aún  no hay canciones para escuchar.")
        return

    print("--------------------------------\n")
    print("\n Busquedas en la playlist")
    print("--------------------------------\n")
    print("1. Buscar por artista")
    print("2. Buscar por rango de popularidad")
    
    op_b = input("Seleccione una opción (1 o 2): ")

    if op_b == '1':
        art_b = input("Ingrese el nombre del artista a buscar: ").strip().title()
        resultados = []
        for i, artista_item in enumerate(art):
            if art_b in artista_item:
                resultados.append((nm[i], art[i], plrs[i]))
        
        if resultados:
            print(f"\nResultados para '{art_b}':")
            for nombre_res, art_res, pop_res in resultados:
                print(f"'{nombre_res}' de {art_res} (Popularidad: {pop_res})")
        else:
            print(f"No se encontraron canciones del artista '{art_b}'.")

    elif op_b == '2':
        while True:
            try:
                min_pop = int(input("Ingrese la popularidad mínima (1-100): "))
                max_pop = int(input("Ingrese la popularidad máxima (1-100): "))
                if not (1 <= min_pop <= 100 and 1 <= max_pop <= 100 and min_pop <= max_pop):
                    print("Asegúrese de que los rangos sean válidos (1-100) y el mínimo sea menor o igual al máximo.")
                    continue
                break
            except ValueError:
                print("Ingrese números enteros válidos.")
        
        resultados = []
        for i, pop_item in enumerate(plrs):
            if min_pop <= pop_item <= max_pop:
                resultados.append((nm[i], art[i], pop_item))

        if resultados:
            print(f"\nResultados para rango de popularidad {min_pop}-{max_pop}:")
            for nombre_res, art_res, pop_res in resultados:
                print(f"'{nombre_res}' de {art_res} (Popularidad: {pop_res})")
        else:
            print("No se encontraron canciones en ese rango de popularidad.")
            
    else:
        print("Opción de búsqueda no válida.")

def plts():
    if not nm:
        print("No hay canciones registradas.")
        return

    prom = sum(plrs) / len(plrs)
    recomendadas = []

    for i, pop_item in enumerate(plrs):
        if pop_item > prom:
            recomendadas.append((nm[i], art[i], plrs[i]))

    print(f"\n Recomendaciones (Popularidad > {prom:.2f}) ")
    if recomendadas:
        for nombre_res, art_res, pop_res in recomendadas:
            print(f"'{nombre_res}' de {art_res} (Popularidad: {pop_res})")
    else:
        print("Ninguna canción supera el promedio de popularidad elegido.")

def main():
    while True:
        menu()
        op = input("Seleccione una opción (1-5): ")
        
        if op == '1':
            agg_c()
        elif op == '2':
            rpts()
        elif op == '3':
            filtro()
        elif op == '4':
            plts()
        elif op == '5':
            print("Te invitamos a cslificar el servicio de playlist vistando la pagina web")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()


