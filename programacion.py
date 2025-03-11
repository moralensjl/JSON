import json

lenguajes_tipados_1 = {"Nombre": "Java", "Age": 1995}
print(lenguajes_tipados_1)

lenguajes_tipados_2 = {"Nombre": "C#", "Age": 1970}
print(lenguajes_tipados_2)

lenguajes_tipados_3 = {"Nombre": "GoLang", "Age": 2015}
print(lenguajes_tipados_3)


lenguajes_interpretados_1 = {"Nombre": "Javascript", "Age": 1996}
print(lenguajes_interpretados_1)


lenguajes_interpretados_2 = {"Nombre": "PHP", "Age": 1994}
print(lenguajes_interpretados_2)


lenguajes_interpretados_3 = {"Nombre": "Python", "Age": 1991}
print(lenguajes_interpretados_3)


lista_tipados = [lenguajes_tipados_1, lenguajes_tipados_2, lenguajes_tipados_3]
print(lista_tipados)

lista_interpretados = [lenguajes_interpretados_1, lenguajes_interpretados_2, lenguajes_interpretados_3]
print(lista_interpretados)


dicc_tipados_interpretados = {
    "Lenguajes tipados:": lista_tipados,
    "Lenguajes interpretados:": lista_interpretados
}

print(dicc_tipados_interpretados)


lenguajes_programacion = {"Lenguajes de programacion": dicc_tipados_interpretados}
print(lenguajes_programacion)

# Convertir los objetos de python en una cadena de texto en JSON con la funcion dumps.
json_lenguajes = json.dumps(lenguajes_programacion)
print(f'Antes: {lenguajes_programacion}')
print()
print(f'Despues: {json_lenguajes}')


# Le podemos decir por medio de la funcion dumps que nos lo indente
json_lenguajes1 = json.dumps(lenguajes_programacion, indent=4, sort_keys=True)
print(json_lenguajes1)


# Lo podemos guardar en un archivo con la funcion dump (sin 'S')
with open('archivos.json', 'w', encoding='utf-8') as archivo:
    json.dump(lenguajes_programacion, archivo, ensure_ascii=False, indent=4)