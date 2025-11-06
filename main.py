import os
import csv
import re
from constructor_estructura import constructor_estructura
from limpiar_dato import limpiar_dato
from nuevo_item import nuevo_item

#-------------Defino la estructura de la ruta
BASE = "datos"

estructura = {
    "America": {
        "Argentina": ["Mendoza","Buenos Aires","Tucuman"]
    },
    "Europa": {
        "España": ["Madrid","Zaragosa"]
    },
    "Asia": {
        "China": ["Tokyo"]
    },
    "Oceania":{
        "Australia": ["Sydney"]
    },
    "Africa":{
        "Sudafrica": ["Zimbabue"]
    }
}
encabezado = ["habitantes","territorio"] #Defino los encabezados de los csv.
#-------------
creado = constructor_estructura(BASE,estructura,encabezado)
menu = True
while menu:
    print("(1)->Alta de nuevo item")
    print("(2)->Mostrar items totales y filtrado")
    print("(3)->Modificación de item")
    print("(2)->Eliminación de item")
    print("(2)->Funcionalidades adicionales")
    print("(3)->Salir")
    try:
        opcion = int(input("Ingresa una opción: "))
    except ValueError:
        print("Carcater incorrecto, ingresa un numero.")
    match opcion:
        case 1:
            nuevo_item(estructura,BASE,encabezado)
        case 2:
            print("hola")
        case 3:
            print("hola")
        case 4:
            print("hola")
        case 5:
            print("hola")
        case 6:
            print("Saliendo del programa...")
            break
                
