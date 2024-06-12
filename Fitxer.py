# Función para leer una lista de elementos desde la entrada del usuario.
def leer_lista():
    a = 'l'
    l = []
    while a != '.':
        a = input("Introduce la lista, para terminarla mete un . : ") 
        if a != '.':
            l.append(a)
        else:
            return l

# Función para crear un fichero y escribir una lista de elementos en él.
def crear_fichero():
    with open("Lista_de_Compra.txt", "w") as f:
        f.write("Lista de compra:\n") 
        for e in leer_lista():  # Itera sobre cada elemento de la lista obtenida de leer_lista().
            f.write(e + "\n")  # Escribe cada elemento en una nueva línea del fichero.
    print("Fichero creado y elementos añadidos.")

# Función para agregar un nuevo elemento al fichero existente.
def agregar_elemento():
    with open("Lista_de_Compra.txt", "a") as f:
        elemento = input("Introduce el nuevo elemento a agregar: ")
        f.write(elemento + "\n")  # Escribe el nuevo elemento en una nueva línea del fichero.
    print("Elemento agregado.")

# Función para modificar un elemento existente en el fichero.
def modificar_elemento():
    with open("Lista_de_Compra.txt", "r") as f:
        lineas = f.readlines()  # Lee todas las líneas del fichero y las almacena en una lista.
    
    mostrar_contenido()
    indice = int(input("Introduce el número del elemento a modificar (empezando desde 0): ")) + 1
    nuevo_valor = input("Introduce el nuevo valor: ")
    
    if 1 <= indice < len(lineas):  # Verifica que el índice esté dentro del rango válido.
        lineas[indice] = nuevo_valor + "\n"  # Actualiza la línea correspondiente con el nuevo valor.
        with open("Lista_de_Compra.txt", "w") as f:
            f.writelines(lineas)  # Escribe todas las líneas de vuelta en el fichero.
        print("Elemento modificado.")
    else:
        print("Índice no válido.")

# Función para eliminar un elemento del fichero.
def eliminar_elemento():
    with open("Lista_de_Compra.txt", "r") as f:
        lineas = f.readlines()  # Lee todas las líneas del fichero y las almacena en una lista.
    
    mostrar_contenido()
    indice = int(input("Introduce el número del elemento a eliminar (empezando desde 0): ")) + 1
    
    if 1 <= indice < len(lineas):  # Verifica que el índice esté dentro del rango válido.
        lineas.pop(indice)  # Elimina la línea correspondiente de la lista.
        with open("Lista_de_Compra.txt", "w") as f:
            f.writelines(lineas)  # Escribe todas las líneas de vuelta en el fichero.
        print("Elemento eliminado.")
    else:
        print("Índice no válido.")

# Función para mostrar el contenido del fichero.
def mostrar_contenido():
    with open("Lista_de_Compra.txt", "r") as f:  # Abre el fichero en modo lectura.
        lineas = f.readlines()  # Lee todas las líneas del fichero.
        for i, linea in enumerate(lineas):  # Itera sobre cada línea con su índice.
            print(f"{i - 1}. {linea.strip()}" if i > 0 else linea.strip())  # Muestra el contenido, ajustando el índice para los elementos.

# Función principal que muestra un menú y permite seleccionar diferentes opciones.
def PP():
    while True:
        print("\n1. Crear fichero y añadir lista inicial")
        print("2. Agregar elemento")
        print("3. Modificar elemento")
        print("4. Eliminar elemento")
        print("5. Mostrar contenido")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")
        
        match opcion:  # Ejecuta una acción según la opción seleccionada.
            case '1':
                crear_fichero()
            case '2':
                agregar_elemento()
            case '3':
                modificar_elemento()
            case '4':
                eliminar_elemento()
            case '5':
                mostrar_contenido()
            case '6':
                break
            case other:
                print("Opción no válida. Inténtalo de nuevo.")