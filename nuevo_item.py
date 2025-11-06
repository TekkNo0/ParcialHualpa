import csv
import os 

def nuevo_item(estructura, base, encabezado):
    continente = input("Ingrese el continente al que quiere añadir país: ").capitalize()
    
    if continente in estructura:
        pais = input("Ingrese el nuevo país a añadir: ").capitalize()
        
        if pais not in estructura[continente]: # Si el país no está, entra en la condicion
            estructura[continente][pais] = []
            print(f"País {pais} añadido al continente {continente}.")
        
        provincia = input("Ingrese la provincia o estado a añadir: ").capitalize()
        
        if provincia not in estructura[continente][pais]: # Si la provincia no existe dentro del país, la agregamos
            estructura[continente][pais].append(provincia)
            
            ruta_continente = os.path.join(base, continente) # Creo carpetas
            ruta_pais = os.path.join(ruta_continente, pais)
            os.makedirs(ruta_pais, exist_ok=True)
            
            archivo = os.path.join(ruta_pais, f"{provincia}.csv") # Archivo CSV para esa provincia
            
            poblacion = input(f"Ingresa la población de {provincia}: ")
            territorio = input(f"Ingresa el territorio de {provincia}: ")
            
            with open(archivo, "w", newline="", encoding="utf-8") as f: # Crear el CSV de la provincia
                writer = csv.writer(f)
                writer.writerow(encabezado)
                writer.writerow([poblacion, territorio])
            
            print(f"Provincia {provincia} añadida.")
        
        else:
            print("Provincia ya registrada.")
    
    else:
        print("Continente no válido.")
