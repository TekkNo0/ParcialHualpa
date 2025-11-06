import os
import csv
import re
from estructura_actualizada import cargar_estructura
from constructor_estructura import constructor_estructura
from limpiar_dato import limpiar_dato
from nuevo_item import nuevo_item
from mostrar_datos import mostrar_items
from modificar_estructura import modificar_item
from eliminar_item import eliminar_item
from funcionalidades import funcionalidades_adicionales

#-------------Defino la estructura de la ruta
BASE = "datos"
encabezado = ["habitantes","territorio"] #Defino los encabezados de los csv.
creado = constructor_estructura
estructura = cargar_estructura(BASE)
#-------------

menu = True
while menu:
    print("\n(1)->Alta de nuevo item")
    print("(2)->Mostrar items totales y filtrado")
    print("(3)->Modificación de item")
    print("(4)->Eliminación de item")
    print("(5)->Funcionalidades adicionales")
    print("(6)->Salir\n")
    try:
        opcion = int(input("Ingresa una opción: "))
    except ValueError:
        print("Carcater incorrecto, ingresa un numero.")
    match opcion:
        case 1:
            nuevo_item(estructura,BASE,encabezado)
        case 2:
            mostrar_items(estructura)
        case 3:
            modificar_item(estructura, BASE)
        case 4:
            eliminar_item(estructura,BASE)
        case 5:
            funcionalidades_adicionales(BASE)
        case 6:
            print("Saliendo del programa...")
            break
                
