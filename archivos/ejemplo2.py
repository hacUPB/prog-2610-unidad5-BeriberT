fp = open(".\\archivos\\vi.txt", "r", encoding="utf-8")
datos_1 = fp.readlines()
for i in datos_1:
    print(i[0])

fp.close()