import csv
import os
import re
from limpiar_dato import limpiar_dato
#Creo función que crea los archivos y construye la ruta en el SO de estos.
def constructor_estructura(base,estructura,encabezado=None):
    if encabezado is None:
        encabezado = ["habitantes","territorio"] #Por si no se pasa un encabezado, la función va a usar un encabezado por defecto.
    
    for clave, valor in estructura.items(): 
        carpeta = limpiar_dato(clave)#Limpio la clave del dict y lo guardo en carpeta        
        ruta = os.path.join(base,carpeta) # Construye la ruta para el SO. ej: datos/America
        try:
            os.makedirs(ruta, exist_ok=True) #Creo el directorio de "datos" y exist_ok=true me evita errores si la carpeta ya existe.
        except Exception as error: #Si hay un error, se guarda como "error".
            print("No se pudo crear la carpeta",ruta,"->",error)
            continue
        if isinstance(valor, dict): #Caso de recursividad
            constructor_estructura(ruta, valor, encabezado) #Ahora la base es la ruta por lo que baja un nivel, 
        elif isinstance(valor, (list,tuple)): #Valor contiene nombre de ciudades
            for i in valor: 
                archivo = os.path.join(ruta, limpiar_dato(i) + ".csv") #Construye la ruta del archivo y se agrega el .csv
                try:
                    with open(archivo,"w",newline="",encoding="utf-8") as f: #Abro el archivo en modo de escritura
                        writer = csv.writer(f)
                        writer.writerow(encabezado) #Escribe el encabezado
                        
                except Exception as error: #Control de errores
                    print("No se pudo crear el archivo",archivo,"->", error)
        else:
            print("Valor no soportado.",{type(valor)})