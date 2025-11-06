import csv
import os

def modificar_item(estructura, base):
    continente = input("Ingrese el continente: ").capitalize()
    if continente not in estructura: #Validaciones para comprobar si lo requerido esta en la estructura
        print("Continente no encontrado.")
        return

    pais = input("Ingrese el país: ").capitalize()
    if pais not in estructura[continente]:
        print("País no encontrado.")
        return

    provincia = input("Ingrese la provincia o estado: ").capitalize()
    if provincia not in estructura[continente][pais]:
        print("Provincia no encontrada.")
        return

    
    archivo = os.path.join(base, continente, pais, f"{provincia}.csv") # Ruta del archivo CSV

    if not os.path.exists(archivo): #Validación
        print("El archivo CSV de la provincia no existe.")
        return

    nueva_poblacion = input("Nueva población (dejar vacío para mantener actual): ")  # Pedir nuevos valores
    nuevo_territorio = input("Nuevo territorio (dejar vacío para mantener actual): ")


    with open(archivo, "w", newline="", encoding="utf-8") as f:  # Escribimos los cambios
        writer = csv.DictWriter(f, fieldnames=["poblacion", "territorio"])
        writer.writeheader()
        writer.writerow({
            "poblacion": nueva_poblacion,
            "territorio": nuevo_territorio
        })

    print(f"\nDatos de {provincia} actualizados correctamente.")
