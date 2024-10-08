### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:  # Es opcional
    print("Mi condición es mayor o igual que 10")

print("-"*30)

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("-"*30)

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

print("-"*30)

my_tuple = (20, 1.85, "César", "Salas", "Enrique")

for element in my_tuple:
    print(element)

print("-"*30)

my_set = {"César", "Salas", 20}

for element in my_set:
    print(element)

print("-"*30)

my_dict = {"Nombre": "César", "Apellido": "Salas", "Edad": 20, 1: "Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bluce for para diccionario ha finalizado")

print("-"*30)

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")