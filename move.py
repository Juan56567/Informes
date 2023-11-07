import os
import shutil

lm = "C:/Users/Lenovo/Dropbox/03. PRODUCCION ORDEN DE TRABAJO"
lf = "C:/Users/Lenovo/Dropbox/Aplicaciones/Kizeo Forms/DIAGNOSTICOS"


direcciones = {
    carpeta[0:4]: lm + "/" + carpeta + "/" + "REGISTRO FOTOGRAFICO/1. DIAGNOSTICO"
    for carpeta in os.listdir(lm)
}
fDirecciones = {carpeta: lf + "/" + carpeta for carpeta in os.listdir(lf)}


for x in fDirecciones:
    try:
        cantidadFotos = len(os.listdir(fDirecciones[x]))
        destino = len(os.listdir(direcciones[x]))
        fotos = [fDirecciones[x] + "/" + foto for foto in os.listdir(fDirecciones[x])]

        if cantidadFotos > destino:
            for i in fotos:
                shutil.move(i, direcciones[x])
            print(x, "se movio exitosamente")
        elif cantidadFotos == destino:
            print(x, "Ya tiene fotos de diagnostico")
        else:
            os.remove(fDirecciones[x])
    except FileNotFoundError:
        print(x, "No se encuentra en la carpeta de produccion")
    except KeyError:
        print(x, "No se encuentra en la carpeta de produccion")
    except PermissionError:
        print(x , " No se puede borrar")