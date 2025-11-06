import os
import csv

def cargar_estructura(base):
    # Crear carpeta base si no existe
    if not os.path.exists(base):
        os.makedirs(base)

    estructura = {}
    continentes = ["America", "Europa", "Asia", "Oceania", "Africa"]

    # Si la carpeta base está vacía, crear los continentes
    if not os.listdir(base):
        for cont in continentes:
            ruta_cont = os.path.join(base, cont)
            os.makedirs(ruta_cont, exist_ok=True)
            estructura[cont] = {}
        return estructura

    # Si ya hay contenido, lo carga
    for continente in continentes:
        ruta_continente = os.path.join(base, continente)
        # Si no existe alguno, lo crea igual
        if not os.path.exists(ruta_continente):
            os.makedirs(ruta_continente)
        estructura[continente] = {}

        # Buscar países dentro del continente
        for pais in os.listdir(ruta_continente):
            ruta_pais = os.path.join(ruta_continente, pais)
            if os.path.isdir(ruta_pais):
                provincias = []
                # Buscar archivos CSV (provincias)
                for archivo in os.listdir(ruta_pais):
                    if archivo.endswith(".csv"):
                        provincias.append(archivo.replace(".csv", ""))
                estructura[continente][pais] = provincias

    return estructura
