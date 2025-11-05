import re
#Limpio los datos para un uso correcto.
def limpiar_dato(s):
    s = s.strip().replace(" ", "_")
    s = re.sub(r"[^\w\-_\.]", "", s) #Para eliminar cualquier caracter no permitido 
    return s