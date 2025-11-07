import csv
import os 

def nuevo_item(estructura, base, encabezado):
    try:
        continente = input("Ingrese el continente al que quiere añadir país: ").capitalize()
        
        if continente in estructura:
            pais = input("Ingrese el nuevo país a añadir: ").capitalize()
            
            # Si el país no está, lo crea
            if pais not in estructura[continente]:
                estructura[continente][pais] = []
                print(f"País {pais} añadido al continente {continente}.")
            
            provincia = input("Ingrese la provincia o estado a añadir: ").capitalize()
            
            # Si la provincia no está registrada, la agrega
            if provincia not in estructura[continente][pais]:
                estructura[continente][pais].append(provincia)
                
                ruta_continente = os.path.join(base, continente)
                ruta_pais = os.path.join(ruta_continente, pais)
                os.makedirs(ruta_pais, exist_ok=True)
                
                archivo = os.path.join(ruta_pais, f"{provincia}.csv")
                
                poblacion = input(f"Ingresa la población de {provincia}: ")
                territorio = input(f"Ingresa el territorio de {provincia}: ")
                
                with open(archivo, "w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(encabezado)
                    writer.writerow([poblacion, territorio])
                
                print(f"Provincia {provincia} añadida correctamente.")
            
            else:
                print("⚠️ Provincia ya registrada.")
        
        else:
            print("❌ Continente no válido.")
    
    except FileNotFoundError:
        print("Error: la ruta base no existe. Verifica la carpeta 'datos'.")
    except PermissionError:
        print("Error: no tienes permisos para escribir en esta ubicación.")
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")