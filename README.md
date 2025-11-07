# ParcialRamiroHualpa
# 6/11/25 entrega.

# El programa organiza los datos de forma jerarquica en carpetas y en archivos CSV. Cada archivo contiene información de las provincias.

# Integrantes del grupo: Maximiliano Monardez, Matias Ruiz y Thiago Oviedo.
#
# Detallamiento de la jerarquia de los datos en las carpetas y archivos csv:
#
# El codigo está modularizado en funciones como: 

# constructor_estructura() -->
# Esta funcion crea los archivos y crea su ruta "SO". Internamente, valida si cuando crea el direct. de datos este ya existe o no, evitando así "pisar" un archivo existente y perder sus datos.

# Función eliminar_item() -->
# Esta función pide datos al usuario y valida si existen en el diccionario "estructura", sinó es el caso entonces devuelve un print de error. También valida si archivos csv no existen, finalmente devolviendo sus respectivos mensajes de tipos de errores gracias a la extructura try-except.

# estructura_actualizada()-->
# Crea la carpeta base que contiene el diccionario principal y sus listas/sublistas. Valida si hay contenido en la lista ruta_continente y crea un espacio vacio si no encuentra datos (entre otras validaciones). finalmente devuelve el diccionario estructura listo para su uso en el programa principal.

# Función funcionalidades_adicionales() -->
# Esta función brinda datos sobre el total de items disponibles en los CSVs actualmente y señala en qué continentes se encuentran c/u. Indica el promedio de habitantes, suma total del territorio disponible, y nos da la opcion de ordenar los datos de los habitantes y territorio de menor a mayor.

# Función limpiar_dato() -->
# Se utiliza en contructor_estructura para eliminar cualquier caracter que pueda provocar errores posteriores en la validacion de datos.

# Función modificar_estructura() -->
# Esta función pide datos al usuario y los guarda modificando/pisando los anteriores, similarmente a la función eliminar_item que elimina items si el user lo desea.

# Función mostrar_datos() -->
# Esta función sirve para que el usuario pueda buscar items existentes o que haya ingresado él, buscandolos efectivamente en "estructura" y sus sublistas y en caso de no encontrarlos lanza un mensaje de validación. Contiene try-except para errores inesperados...

# Función nuevo_item() -->
# Sirve para que el usuario agregue un nuevo país/provincia (o estado) a cierto continente. Valida correctamente si el país/provincia ya existe en los archivos con un mensaje de error. Permite ingresar la superficie y poblacion de la provincia nueva. Por último, cubre las posibles entradas de tipos de datos inesperados por el programa --> int, bool, caracteres extraños.

# Video explicativo y ejemplificador sobre las funciones del programa:
# https://drive.google.com/drive/folders/1bpnj3o0eK5nkg91xtfmVtIwXyUFSBAQ8