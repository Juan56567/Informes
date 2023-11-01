import os
from Informes import auto

# lee las carpetas presentes en la seccion de informes
path = "C:/Users/Lenovo/Downloads/TEST"
dirs = os.listdir(path)


direcciones = {}


# guarda cada ruta en un diccionario con la key del nombre de la carpeta y el valor es el path
for d in dirs:
    direcciones.update({d: path + "/" + d})

# Por cada key en el diccionario accede a la ubicacion de la carpeta y revisa cuantos informes hay por modificar
for tipo in direcciones:
    informes = os.listdir(direcciones[f"{tipo}"])
    location = direcciones[f"{tipo}"]
    if tipo == "BOTELLA" and len(informes) > 0:
        auto(tipo,location)

