import json

# Creamos los diccionarios 
persona1 = {"Nombre": "Moralens", "Edad": 27}
print(persona1)

persona2 = {"Nombre": "Karem", "Edad": 32}
print(persona2)


cargos_persona1 = {"Cargo": "Software engeneer", "Lenguajes": "Python"}
print(cargos_persona1)


cargos_persona2 = {"Cargo": "Frontend developer", "Lenguajes": "Javascript"}
print(cargos_persona2)

# Luego creamos una lista donde introducimos los diccionarios que hemos creado
lista_cargos_persona1 = [persona1, cargos_persona1]
print(lista_cargos_persona1)


lista_cargos_persona2 = [persona2, cargos_persona2]
print(lista_cargos_persona2)


# Esa lista lo ponemos en otro diccionario
datos_personales = {
    "Datos sobre Moralens": lista_cargos_persona1,
    "Datos sobre Karem": lista_cargos_persona2
}

print(datos_personales)

datos_empleados = {
    "Datos de empleados": datos_personales
}

print("\n", datos_empleados) 

# Convertimos los objetos de python en una cadena

json_datos = json.dumps(datos_empleados)
print("\nDatos como cadena en JSON:\n ", json_datos)


# Podemos indentar esos datos: ponemos la variable, luego indent, y por ultimo sort_keys
json_datos = json.dumps(datos_empleados, indent=4, sort_keys=True)
print(json_datos)

# Podemos guardar esos datos en un archivo
# Al guardarlo como un archivo tenemos que dar algunos pasos:
# 1) con with open creamos el nombre del archivo
# 2) con la intruccion 'w' le decimos que escriba el archivo
# 3) Le colocamos el utf-8 para que acepte los caracteres extranos
# 4) Finalmente le colocamos un alias a ese archivo
# 5) Luego llamamos la funcion dumps donde pondremos los siguientes datos:
# a) La variable donde se encuentra los archivos de json que han sido convertidos
# b) Colocamos el alias que tendra el archivo 
# c) ensure_ascii
# d) luego le pedimos que nos lo indente
with open('Datos-empleados.json', 'w', encoding='utf-8') as archivo:
    json.dump(datos_empleados, archivo, ensure_ascii=False, indent=4)
     
     