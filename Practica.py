import graphviz

# Función que lee el archivo de texto plano y retorna una lista de diccionarios con la información de cada película
def leer_archivo(nombre_archivo):
    peliculas = []
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            datos = linea.strip().split(';')
            pelicula = {
                'nombre': datos[0],
                'actores': datos[1].split(','),
                'año': datos[2],
                'género': datos[3]
            }
            peliculas.append(pelicula)
    return peliculas

# Función que muestra todas las películas
def mostrar_peliculas(peliculas):
    if not peliculas:
        print("No hay películas para mostrar.")
    else:
        for pelicula in peliculas:
            print(f"Nombre: {pelicula['nombre']}")
            print(f"Actores: {', '.join(pelicula['actores'])}")
            print(f"Año de estreno: {pelicula['año']}")
            print(f"Género: {pelicula['género']}")
            print("\n")

# Función que muestra una lista de películas enumeradas y permite al usuario seleccionar una para desplegar los actores
def Mostrar_actores(peliculas):
    print("Películas disponibles:\n")
    for i, pelicula in enumerate(peliculas):
        print(f"{i + 1}. {pelicula['nombre']}")
    
    # Solicita al usuario que seleccione una película
    while True:
        try:
            seleccion = int(input("\nIngrese el número de la película que desea ver los actores: "))
            if seleccion < 1 or seleccion > len(peliculas):
                print("Ingrese un número válido.")
                continue
            break
        except ValueError:
            print("Ingrese un número válido.")
    
    # Muestra los actores de la película seleccionada
    pelicula_seleccionada = peliculas[seleccion - 1]
    print(f"\nActores de la película '{pelicula_seleccionada['nombre']}':\n")
    for actor in pelicula_seleccionada['actores']:
        print(f"- {actor}")

# Función que muestra todas las películas en las que un actor en particular haya participado
def mostrar_peliculas_por_actor(peliculas, actor):
    peliculas_filtradas = [p for p in peliculas if p['actores'] == actor]
    print(peliculas_filtradas)
    for pelicula in peliculas_filtradas:
        print(f"Nombre: {pelicula['nombre']}")
        print(f"Actores: {','.join(pelicula['actores'])}")
        print(f"Año de estreno: {pelicula['año']}")
        print(f"Género: {pelicula['género']}")
        print("\n")

def mostrar_peliculas_por_anho(peliculas, anho):
    peliculas_filtradas = [p for p in peliculas if p['año'] == anho]
    for pelicula in peliculas_filtradas:
        print(f"Nombre: {pelicula['nombre']}")
        print(f"Actores: {','.join(pelicula['actores'])}")
        print(f"Año de estreno: {pelicula['año']}")
        print(f"Género: {pelicula['género']}")
        print("\n")

# Función que muestra todas las películas de un género en particular
def mostrar_peliculas_por_genero(peliculas, genero):
    peliculas_filtradas = [p for p in peliculas if p['género'] == genero]
    for pelicula in peliculas_filtradas:
        print(f"Nombre: {pelicula['nombre']}")
        print(f"Actores: {','.join(pelicula['actores'])}")
        print(f"Año de estreno: {pelicula['año']}")
        print(f"Género: {pelicula['género']}")
        print("\n")

# Función que genera un diagrama de flujo utilizando Graphviz
def generar_diagrama(peliculas):
    diagrama = graphviz.Digraph(comment='Películas')
    
    # Agrega cada actor como un nodo en el diagrama
    for pelicula in peliculas:
        nombre = pelicula['nombre']
        actores = ",".join(pelicula['actores'])
        año = pelicula['año']
        género = pelicula['género']
        
        # Crea el nodo correspondiente a la película

        # Crea el nodo correspondiente a la película
        diagrama.node(nombre,label=f"{nombre}\nAño: {año}\nGénero: {género}",color="green")
        for actor in pelicula['actores']:
            for pelicula2 in peliculas:
                for otro_actor in pelicula2['actores']:
                    if actor != otro_actor and actor in pelicula2['actores']:
                        diagrama.node(actor,label=otro_actor,color="yellow")
        break

    
    # Agrega las relaciones entre películas al diagrama
    for pelicula in peliculas:
        for actor in pelicula['actores']:
                if actor in pelicula['actores']:
                    # Crea una relación entre la película y la otra película que comparte el mismo actor
                    diagrama.edge(pelicula['nombre'], actor)
    
    # Renderiza el diagrama y lo muestra en pantalla
    diagrama.render('diagrama', view=True)

# Función que presenta el menú al usuario y solicita una opción
def presentar_menu():
    print("Bienvenido al programa de películas!")
    print("Por favor, seleccione una opción:")
    print("1 - Cargar archivos")
    print("2 - Gestionar películas")
    print("3 - Filtrar")
    print("4 - Generar diagrama de relaciones entre las películas")
    print("5 - Salir")
    opcion = input("Opción seleccionada: ")
    return opcion

def presentar_menu_gestion():
    print("a - Mostrar Películas")
    print("b - Mostrar Actores")
    print("c - Regresar")
    opcion_menu2 = input("Opción seleccionada: ")
    return opcion_menu2

def presentar_menu_filtrado():
    print("a - Filtrado por actor")
    print("b - Filtrado por año")
    print("c - Filtrado por género")
    print("d - Regresar")
    opcion_menu3 = input("Opción seleccionada: ")
    return opcion_menu3

print("Lenguajes Formales y de Programación")
print("Sección A-")
print("Carné 201901815")
print("Ivan de Jesús Pisquiy Escobar")
# Función principal del programa
def main():
    opcion = presentar_menu()
    while opcion != '5':
        if opcion == '1':
            archivo = input("Ingrese el nombre del archivo a leer: ")
            peliculas = leer_archivo(archivo)
        elif opcion == '2':
            opcion_menu2 = presentar_menu_gestion()
            while opcion_menu2 != 'c':
                opcion_menu2 == ""
                if opcion_menu2 == "a":
                    mostrar_peliculas(peliculas)
                elif opcion_menu2 == "b":
                    Mostrar_actores(peliculas)
                else:
                    print("Opción no válida")
                opcion_menu2 = presentar_menu_gestion()
        elif opcion == '3':
            opcion_menu3 = presentar_menu_filtrado()
            while opcion_menu3 != "d":
                if opcion_menu3 == "a":
                    actor = input("Ingrese el nombre del actor a buscar: ")
                    mostrar_peliculas_por_actor(peliculas, actor)
                elif opcion_menu3 == "b":
                    anho = input("Ingrese el año a buscar: ")
                    mostrar_peliculas_por_anho(peliculas, anho)
                elif opcion_menu3 == "c":
                    genero = input("Ingrese el género a buscar: ")
                    mostrar_peliculas_por_genero(peliculas, genero)
                else:
                    print("Opción no válida")
                opcion_menu3 = presentar_menu_filtrado()
        elif opcion == '4':
            generar_diagrama(peliculas)
            print("Diagrama generado con éxito!")
        else:
            print("Opción inválida, por favor seleccione una opción válida.")
        opcion = presentar_menu()
    print("Gracias por utilizar este programa! c:")

# Ejecutamos la función principal
if __name__ == '__main__':
    main()
