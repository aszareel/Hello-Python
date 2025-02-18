# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=23822

### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:  # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("La ejecución continúa")

# For
print('my_list---------------------------------------------')
my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

print('my_tuple---------------------------------------------')
my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
    print(element)

print('my_set---------------------------------------------')
my_set = {"Brais", "Moure", 35}

for element in my_set:
    print(element)

print('my_dict---------------------------------------------')
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para diccionario ha finalizado")

print("La ejecución continúa")

print('---------------------------------------------')
for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")
