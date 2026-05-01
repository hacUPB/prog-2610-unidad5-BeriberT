# # Forma antigua
# f = open("datos.txt", "r")
# contenido = f.read()
# f.close()

# # Forma moderna (Recomendada)
# with open("datos.txt", "r") as f:
#     contenido = f.read()
# # ¡Ya está cerrado automáticamente aquí!

# nombre_archivo = input("Nombra tu nuevo archivo (ej: diario.txt): ")

# # Contexto de escritura
# with open(nombre_archivo, 'w') as archivo:
#     datos = input("Escribe tu primer secreto: ")
#     archivo.write(datos)

# # Contexto de lectura
# with open(nombre_archivo, 'r') as archivo:
#     print("\n--- Leyendo tu archivo ---")
#     print(archivo.read())