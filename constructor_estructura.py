import csv
import os
import re
from limpiar_dato import limpiar_dato

def constructor_estructura(base,estructura,encabezado=None):
    if encabezado is None:
        encabezado = ["habitantes","poblacion"] #Por si no se pasa un encabezado, la función va a usar un encabezado por defecto.
    
    for clave, valor in estructura.items(): 
        carpeta = limpiar_dato(clave)#Limpio la clave del dict y lo guardo en carpeta        
        ruta = os.path.join(base,carpeta) # Construye la ruta para el SO. ej: datos/America
        try:
            os.makedirs(ruta, exist_ok=True) #Creo el directorio de "datos" y exist_ok=true me evita errores si la carpeta ya existe.
        except Exception as error: #Si hay un error, se guarda como "error".
            print("No se pudo crear la carpeta",ruta,"->",error)
            continue
        if isinstance(valor, dict):
            constructor_estructura(ruta, valor, encabezado)
            
        elif isinstance(valor, (list,tuple)):
            for i in valor:
                archivo = os.path.join(ruta, limpiar_dato(i) + ".csv")
                try:
                    with open(archivo,"w",newline="",encoding="utf-8") as f:
                        writer = csv.writer(f)
                        writer.writerow(encabezado)
                    print("Archivo creado.")
                        
                except Exception as error:
                    print("No se pudo crear el archivo",archivo,"->", error)
        else:
            print("Valor no soportado.",{type(valor)})

