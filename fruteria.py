import json

dicc_frutas_1 = {"Nombre": "Naranja", "Cantidad": 30}
print(dicc_frutas_1)

dicc_frutas_2 = {"Nombre": "Manzana", "Cantidad": 20}
print(dicc_frutas_2)

dicc_frutas_3 = {"Nombre": "Piña", "Cantidad": 45}
print(dicc_frutas_3)


dicc_verdura_1 = {"Nombre": "Lechuga", "Cantidad": 32}
print(dicc_verdura_1)

dicc_verdura_2 = {"Nombre": "Broccoli", "Cantidad": 30}
print(dicc_verdura_2)

dicc_verdura_3 = {"Nombre": "Pepino", "Cantidad": 40}
print(dicc_verdura_3)

lista_fruta = [dicc_frutas_1, dicc_frutas_2, dicc_frutas_3]
print(lista_fruta)

lista_verdura = [dicc_verdura_1, dicc_verdura_2, dicc_verdura_3]
print(lista_verdura)

dicc_fruta_verdura = {
    "Fruta": lista_fruta,
    "Verdura": lista_verdura
}

print(dicc_fruta_verdura)


dicc_fruteria = {"Fruteria": dicc_fruta_verdura}
print(dicc_fruteria)


dicc_fruteria_1= {"Fruteria":



 {"Fruta":
 
 [{"Nombre": "Naranja", "'Cantidad'": 30},
  {"Nombre": "Manzana", "Cantidad": 20}, 
  {"Nombre": "Pina", "Cantidad": 45}],


  "Verdura": 


  [{"Nombre": "Lechuga", "Cantidad": 32},
   {"Nombre": "Broccoli", "Cantidad": 30}, 
   {"Nombre": "Pepino", "Cantidad": 40}
   
   ]
   
   }

}


# Imprimimos por pantalla el tipo y los datos
print('Tipo de los datos', type(dicc_fruteria_1))
print('\nDatos en estructuras de datos de python (diccionario):\n')
print(dicc_fruteria_1)


# Una vez que tenemos la estructura creada, la codificamos en JSON (dumps)
# Nos devuelve el string con el json
json_fruteria = json.dumps(dicc_fruteria_1) # Tipo de los datos: <class 'str'>
print("Tipo de los datos:", type(json_fruteria))
print("\nDatos en JSON:\n")
print(json_fruteria)


# Tambien podemos pedirle a dumps que nos lo indente por nosotros o que nos ordene las claves
json_fruteria_indentado = json.dumps(dicc_fruteria_1, indent=4, sort_keys=True)
print(json_fruteria_indentado)

# Diferencias
print(dicc_fruteria)
print()
print(dicc_fruteria_1)


# Lo podemos guadar en un fichero 
with open('data.json', 'w', encoding='utf-8') as fichero:
    json.dump(dicc_fruteria_1, fichero, ensure_ascii=False, indent=4)


with open('data2.json', 'w', encoding='utf-8') as f:
    json.dump(dicc_fruteria, f, ensure_ascii=False)



# DECODIFICAR JSON (json_loads(String))
# Ahora veremos el caso contrario, dado un dato en formato JSON, 
# veremos como decodificarlo para transformarlo en tipos de datos manejables 
# por Python. Para ello usaremos la función json_loads(String)


# Disponemos de JSON fruteria el cual contiene informacion en formato JSON
print('Tipo de los datos: ', type(json_fruteria))
print('\nDatos en JSON: \n')
print(json_fruteria)

f_dicc = json.loads(json_fruteria)
print('Tipo de los datos: ', type(f_dicc))
print('\nDatos en estructuras de datos de python (diccionarios): \n')
print(f_dicc)



# Y si queremos lo podemos abrir desde un fichero
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    print(type(data))
    print(data)