def mostrar_items(estructura):
    print("1. Mostrar todo")
    print("2. Filtrar por continente")
    print("3. Filtrar por país")

    try:
        opcion = int(input("Ingresa una opción: "))
    except ValueError:
        print("Caracter incorrecto, ingresa un numero.")
        return
    try:
        match opcion:
            case 1:
                for continente, paises in estructura.items(): #Recorre items de estructura y los muestra
                    print(f"Continente: {continente}")
                    for pais, provincias in paises.items():
                        print(f"{pais}: {provincias}")
            case 2:
                cont = input("Ingrese el continente: ").capitalize() #Filtra por continente si es que el continente ingresado esta en la estructura
                if cont in estructura:
                    print(f"{cont}: ")
                    if not estructura[cont]:
                        print("No hay paises asignados.")
                    else:
                        for pais, provincias in estructura[cont].items():
                            print(f"{pais}: {provincias}")
                else:
                    print("Continente no encontrado.")
            case 3:
                pais_buscar = input("Ingrese el pais a buscar: ").capitalize() #Recorreitems de estructura y devuelve los items correspondientes.
                encontrado = False
                for continente, paises in estructura.items():
                    if pais_buscar in paises:
                        provincias = paises[pais_buscar]
                        print(f"->{continente} \n{pais_buscar}: {provincias}")
                        encontrado = True
                if not encontrado:
                    print("Pais no encontrado.")
            case _:
                print("Opción Invalida.")
    except Exception as error:
        print(f"Error: {error}")