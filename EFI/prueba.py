from json import loads

a = open("parciales/EFI/data.json")
s = a.read()

data = loads(s)

categorias = ["Nombre","Pais","Mail","Curso","Telefono"]

for dic in data:
    for key,value in dic.items():
        print(key," : ",value)
        
print("###########################################################")

""" for dic in data:
    for value in dic.values():
        if value == "Argentina":
            print(dic) """
