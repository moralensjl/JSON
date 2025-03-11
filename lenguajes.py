import json

lenguajes_tipados = ['Go', 'Typescript', 'Java', 'C#']
print(lenguajes_tipados)

lenguajes_interpretados = ['Javascript', 'Python', 'PHP', 'Ruby']
print(lenguajes_interpretados)


dicc_lenguajes = {
    'Tipados': lenguajes_tipados,
    'Interpretados': lenguajes_interpretados
}

print(dicc_lenguajes)

lenguajes_programacion = ['Lenguajes de programacion', dicc_lenguajes]
print(lenguajes_programacion)

# Convertir los objetos de python en una cadena de texto en JSON con la funcion dumps.

json_lenguajes = json.dumps(lenguajes_programacion)
print('Tipos de datos', type(json_lenguajes)) # <class 'str'>


# Convertir un objeto de python en un archivo JSON. Lo podemos guardar en un archivo.

with open('archivo.json', 'w', encoding='utf-8') as archivo:
    json.dump(json_lenguajes, archivo, ensure_ascii=False, indent=4)


# Vamos a indentarlo
json_indentado = json.dumps(json_lenguajes, indent=4, sort_keys=True)
print(json_indentado)