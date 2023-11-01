import os
from Informes import auto
from Objetos import *
import time

inicio = time.time()


location = "C:/Users/Lenovo/Downloads/TEST"
directorios = os.listdir(location)
direcciones = {}
counter = 0


for carpeta in directorios:
    ruta = location + "/" + carpeta
    direcciones.update({carpeta: ruta})

# Buscar la conatidad de informes en cada tipo de informe
print("Cargando")
for i in direcciones:
    if i == "BOTELLA":
        informes = os.listdir(direcciones[i])
        for doc in informes:
            tempLoc = direcciones[i] + "/" + doc
            b = Botella(tempLoc)
            b.automatizar()
            counter += 1
        print("Botella terminados")

    elif i == "TELESCOPICOS":
        informes = os.listdir(direcciones[i])
        for doc in informes:
            tempLoc = direcciones[i] + "/" + doc
            tc = Telescopico(tempLoc)
            tc.automatizar()
            counter += 1
        print("Telescopicos terminados")
    # elif i == "TIRANTES":
    #     informes = os.listdir(direcciones[i])
    #     for doc in informes:
    #         tempLoc = direcciones[i] + "/" + doc
    #         t = Telescopico(tempLoc)
    #         t.automatizar()
print("Informes terminados")
fin = time.time()
duracion = round(fin - inicio, 1)
print(f"Se realizaron {counter} informes en {duracion} segundos")
