import os
from Objetos import *
import time

inicio = time.time()
location = "C:/Users/Lenovo/Dropbox/Aplicaciones/Kizeo Forms/INFORMES"

counter = 0
direcciones = {carpeta : location + "/" + carpeta for carpeta in os.listdir(location)}

# Buscar la conatidad de informes en cada tipo de informe
print("Cargando")
for i in direcciones:
    if i == "BOTELLA":
        informes = os.listdir(direcciones[i])
        for doc in informes:
            tempLoc = direcciones[i] + "/" + doc
            b = Botella(tempLoc)
            b.automatizar()
            print(doc)
            counter += 1

    elif i == "TELESCOPICOS":
        informes = os.listdir(direcciones[i])
        for doc in informes:
            tempLoc = direcciones[i] + "/" + doc
            tc = Telescopico(tempLoc)
            tc.automatizar()
            print(doc)
            counter += 1

    elif i == "TIRANTES":
        informes = os.listdir(direcciones[i])
        for doc in informes:
            tempLoc = direcciones[i] + "/" + doc
            tt = Tirantes(tempLoc)
            tt.automatizar()
            print(doc)
            counter += 1
    
    elif i == "BUZOS":
        informes = os.listdir(direcciones[i])
        for doc in informes:
            tempLoc = direcciones[i] + "/" + doc
            bz = Buzo(tempLoc)
            bz.automatizar()
            print(doc)
            counter += 1
    else:
        pass


fin = round((time.time() - inicio),3)

print(counter," Informes listos para revisión" , fin)

