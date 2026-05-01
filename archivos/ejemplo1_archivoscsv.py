import csv

# 1. Abrimos el archivo asegurando la codificación correcta
with open('.\\archivos\\armas.csv', mode='r') as archivo:

    # 2. Inicializamos el DictReader
    lector = csv.DictReader(archivo,delimiter=';')

    # 3. Iteramos sobre cada fila del archivo
    for fila in lector:
        # ¡Miren qué fácil es acceder a los datos por su nombre!
        nombre = fila['Nom']
        munición = fila['Cap. mun']
        fabricante = fila['Fabricante']

        print(f"El alumno {nombre} de {fabricante} tiene una capacidad de munición de {munición}.")