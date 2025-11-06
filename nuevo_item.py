import csv
import os 
def nuevo_item(estructura,base,encabezado):
    continente  =  input("Ingrese el continente al que quiere añadir pais: ").capitalize()
    if continente in estructura:
        pais = input("Ingrese el nuevo pais a añadir: ").capitalize()
        if pais not in estructura[continente]:
            estructura[continente][pais] = [] #Creo una lista con el nuevo pais
            provincia = input("Ingrese la provincia o estado a añadir: ")
            if provincia not in estructura[continente][pais]:
                estructura[continente][pais].append(provincia) #Agrego la provincia a la lista
            else:
                print("Provincia ya registrada.")
                return #Si la provincia ya esta registrada sale de la función
            
            poblacion = input(f"Ingresa la población de {pais}: ")
            territorio = input(f"Ingresa el territorio de {pais}: ")
            
            ruta_continente = os.path.join(base,continente) #Creo las carpetas
            ruta_pais = os.path.join(ruta_continente,pais)
            os.makedirs(ruta_pais,exist_ok=True)
            
            #Creo el archivo csv
            archivo = os.path.join(ruta_pais,f"{pais}.csv")
            
            with open(archivo,"w",newline="",encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(encabezado)
                writer.writerow([poblacion,territorio])
            print("Añadido correctamente")
            
        #Si el pais ya existe entra al else    
        else:
            print("Pais ya registrado.")
            provincia = input("Ingrese la provincia o estado a añadir:")
            if provincia not in estructura[continente][pais]:
                estructura[continente][pais].append(provincia)
                
                ruta_pais = os.path.join(base,continente,pais)
                archivo = os.path.join(ruta_pais,f"{pais}.csv")

                
                with open(archivo,"w",newline="",encoding="urf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(encabezado)
                    writer.writerow(poblacion,territorio)
            
    else:
        print("Continente no valido.")
    