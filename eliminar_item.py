import csv
import os

def eliminar_item(estructura, base):
    try:
        continente = input("Ingrese el continente: ").capitalize() #Pide al usuario los datos y los valida
        if continente not in estructura:
            print("Continente no encontrado.")
            return

        pais = input("Ingrese el país: ").capitalize()
        if pais not in estructura[continente]:
            print("País no encontrado.")
            return

        provincia = input("Ingrese la provincia: ").capitalize()
        if provincia not in estructura[continente][pais]:
            print("Provincia no encontrada.")
            return

        ruta_provincia = os.path.join(base, continente, pais, f"{provincia}.csv")

        if not os.path.exists(ruta_provincia):
            print("El archivo CSV de esa provincia no existe.")
            return
        with open(ruta_provincia, "r", encoding="utf-8") as f: #Lee el archivo
            lector = list(csv.DictReader(f))
            if not lector:
                print("No hay ítems para eliminar.") #Si no hay items para eliminar termina.
                return

        eliminado = lector.pop() # Elimina la fila
        
        with open(ruta_provincia, "w", newline="", encoding="utf-8") as f: #Reescribe el archivo CSV ahora sin esa fila
            writer = csv.DictWriter(f, fieldnames=["habitantes", "territorio"])
            writer.writeheader()
            writer.writerows(lector)

        print(f"\nÍtem eliminado correctamente\n")

    except FileNotFoundError: #Validaciones 
        print("Archivo no encontrado.")
    except PermissionError:
        print("No tienes permisos para modificar el archivo.")
    except Exception as e:
        print(f"Error inesperado: {e}")
