import json

persona1 = {"nombre": "moralens jean louis", "edad": 27}
print(persona1)

persona2 = {"nombre": "karem luna", "edad": 32}
print(persona2)

persona3 = {"nombre": "sara hernandez", "edad": 23}
print(persona3)


cargos_persona1 = {"posicion": "frontend developer", "lenguajes": "python, javascript"}
print(cargos_persona1)

cargos_persona2 = {"posicion": "backend developer", "lenguajes": "java, c#"}
print(cargos_persona2)

cargos_persona3 = {"posicion": "backend, frontend developer", "lenguajes": "javascript, node.js"}
print(cargos_persona3)


lista_datos_personales1 = [persona1, cargos_persona1]
print(lista_datos_personales1)

lista_datos_personales2 = [persona2, cargos_persona2]
print(lista_datos_personales1)

lista_datos_personales3 = [persona3, cargos_persona3]
print(lista_datos_personales1)

datos_empleados = {
    "datos de moralens jean louis": lista_datos_personales1,
    "datos de karem luna": lista_datos_personales2,
    "datos de sara hernandez": lista_datos_personales3
}

print(datos_empleados)

datos_empresa = {
    "datos de empleados y sus funciones": datos_empleados
}
print(datos_empresa)


# Vamos a convertir esos objetos de python en una cadena en json
json_cadena = json.dumps(datos_empresa)
print("\nString json", json_cadena)

# Podemos pedirle a la funcion dumps que nos indente el archivo json
json_indentado = json.dumps(datos_empresa, indent=4, sort_keys=True)
print(json_indentado)

# Llamamos a ls funcion dump para que nos pueda crear un archivo
with open('datos-empleado-2.json', 'w', encoding='utf-8') as archivo:
    json.dump(datos_empresa, archivo, indent=4, ensure_ascii=False)
