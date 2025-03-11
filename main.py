import json

def cargar_datos(ruta):
    with open(ruta, encoding= "utf-8") as carpeta:
        cursos = json.load(carpeta)
        print(cursos)


if __name__ == '__main__':
    ruta = 'datos.json'
    cargar_datos(ruta)