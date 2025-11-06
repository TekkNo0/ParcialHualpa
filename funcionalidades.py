import csv, os

def funcionalidades_adicionales(base):
    if not os.path.exists(base):
            print("No hay carpeta base.")
            return
    
    datos = []
    conteo = {}

    for cont in os.listdir(base):
        ruta_cont = os.path.join(base, cont)
        if not os.path.isdir(ruta_cont): continue
        conteo[cont] = 0
        for pais in os.listdir(ruta_cont):
            ruta_pais = os.path.join(ruta_cont, pais)
            if not os.path.isdir(ruta_pais): continue
            for archivo in os.listdir(ruta_pais):
                if archivo.endswith(".csv"):
                    with open(os.path.join(ruta_pais, archivo), encoding="utf-8") as f:
                        for fila in csv.DictReader(f):
                            try:
                                fila["habitantes"] = float(fila["habitantes"])
                                fila["territorio"] = float(fila["territorio"])
                            except: continue
                            fila["continente"], fila["pais"] = cont, pais
                            datos.append(fila)
                            conteo[cont] += 1

    if not datos:
        print("No hay datos disponibles."); return

    print(f"\nTotal ítems: {len(datos)}")
    print(f"Promedio habitantes: {sum(d['habitantes'] for d in datos)/len(datos):.2f}")
    print(f"Suma territorio: {sum(d['territorio'] for d in datos):.2f}\n")

    print("Ítems por continente:")
    for c, n in conteo.items(): print(f" - {c}: {n}")

    op = input("\nOrdenar por (1)Hab↑ (2)Hab↓ (3)Ter↑ (4)Ter↓: ")
    key, rev = ("habitantes", False) if op == "1" else \
                ("habitantes", True) if op == "2" else \
                ("territorio", False) if op == "3" else \
                ("territorio", True)
    for d in sorted(datos, key=lambda x: x[key], reverse=rev):
        print(f"{d['continente']} - {d['pais']}: {d['habitantes']} hab, {d['territorio']} km²")
