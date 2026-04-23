# Lists

my_list = list()
print(type(my_list))

my_other_list = []

print(len(my_list))

my_list = [32, 35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [32, 1.57, "Keyla", "Diaz"]

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list[-4])

print(my_list.count(30)) # para saber cuantas veces se repite
print(my_other_list.index("Keyla"))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3],
print(age)

print(my_list + my_other_list)


my_other_list.append("Argentina") # Insertar otro valor a la lista
print(my_other_list)

my_other_list.insert(1, "rojo") # Insertar otro valor a la lista indicando el index
print(my_other_list)

my_other_list[1] = "black"
print(my_other_list)

my_other_list.remove("black") # Remover un valor de la lista
print(my_other_list)

my_list.remove(30) # Remover un elemento de la lista
print(my_list)

print(my_list.pop()) # Elimina el ultimo elemento
print(my_list)

my_pop_element = my_list.pop(2) # Elimina el elemento del indice indicado
print(my_pop_element)
print(my_list)

del my_list[2] # Elimina por indice
print(my_list)

my_new_list = my_list.copy()

my_list.clear() # Limpiar lista
print(my_list)
print(my_new_list)


my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])

# Tipado dinámico
my_list = "Hola Python"
print(my_list)
print(type(my_list))