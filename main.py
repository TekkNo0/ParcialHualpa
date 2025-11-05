import os
import csv
import re
from constructor_estructura import constructor_estructura
from limpiar_dato import limpiar_dato

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
encabezado = ["habitantes","poblacion"] #Defino los encabezados de los csv.
#-------------

creado = constructor_estructura(BASE,estructura,encabezado)
