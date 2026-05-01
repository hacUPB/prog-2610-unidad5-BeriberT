# import csv

# with open (".\\archivos\\csv.csv","r") as csvfile:
#     lector = csv.reader(csvfile, delimiter=';')
#     for fila in lector:
#         print(fila)

import csv
peso_total = 0
with open (".\\archivos\\csv.csv","r") as csvfile:
    lector = csv.reader(csvfile, delimiter=';')
    encabezado = next(lector)
    for fila in lector:
        peso_total += int(fila[4])
        
print(f"peso total delos aviones:  {peso_total}Kg")