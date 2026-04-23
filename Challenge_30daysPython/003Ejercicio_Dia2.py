# 'Día 2: 30 días de programación en Python'.
# Declara una variable llamada nombre y asígnale un valor.

nombre = "Keyla"

# Declara una variable para el apellido y asígnale un valor.
apellido = "Diaz"

# Declara una variable con nombre completo y asígnale un valor.
nombre_completo = "Keyla Diaz"

# Declara una variable de país y asígnale un valor.
pais = "Argentina"

# Declara una variable de ciudad y asígnale un valor.
ciudad = "Buenos Aires"

# Declara una variable de edad y asígnale un valor.
edad = 32

# Declara una variable de año y asígnale un valor.
año = 2026

# Declara una variable llamada is_married y asígnale un valor.
is_married = False

# Declara una variable llamada is_true y asígnale un valor.
is_true = True

# Declara una variable llamada is_light_on y asígnale un valor.
is_light_on = True

# Declarar varias variables en una sola línea.

libro, autor, editorial, ISBN = "El Poder del Ahora", "Eckhart Tolle", "Grijalbo", 9789502805924

# Comprueba el tipo de datos de todas tus variables usando la función integrada type().
print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(libro))
print(type(autor))
print(type(editorial))
print(type(ISBN))

# Utilizando la función integrada len() , encuentra la longitud de tu nombre.
print(len(nombre))

# Longitud de tu nombre y tu apellido.
print("La longitud del nombre es: ", len(nombre), "Mientras que la longitud del apellido es:", len(apellido))

# Declara 5 como num_one y 4 como num_two.
num_one = 5
num_two = 4

# Suma num_one y num_two y asigna el valor a una variable total.
total = num_one + num_two

# Resta num_two de num_one y asigna el resultado a una variable llamada diff.
diff = num_one - num_two

# Multiplica num_two y num_one y asigna el valor a una variable producto.
producto = num_two * num_one

# Divide num_one entre num_two y asigna el resultado a una variable de división.
division= num_one / num_two

# Utilice la división modular para hallar num_two dividido por num_one y asigne el valor a una variable llamada resto.
resto = num_two % num_one

# Calcula num_one elevado a la potencia de num_two y asigna el valor a una variable exp.
exp = num_one ** num_two

# Calcula la división entera de num_one entre num_two y asigna el valor a una variable llamada floor_division.
floor_division =  num_one // num_two

"""
El radio de un círculo es de 30 metros.
Calcula el área de un círculo y asigna el valor a una variable llamada area_of_circle.
Calcula la circunferencia de un círculo y asigna el valor a una variable llamada circum_of_circle.
Toma el radio como entrada del usuario y calcula el área.

"""
radio=30

# Calcula el área de un círculo
pi = 3.1416
area_of_circle =  pi * (radio ** 2)

# Calcula la circunferencia de un círculo
circum_of_circle = 2 * pi * radio

# Toma el radio como entrada del usuario y calcula el área.
radio = int(input("Indica el valor del radio de un circulo "))
area_of_circle =  pi * (radio ** 2)

"""
Utilice la función de entrada integrada para obtener el 
nombre, apellido, país y edad de un usuario 
y almacene el valor en sus nombres de variables correspondientes.
"""
nombre = input("Ingrese su nombre ")
apellido = input("Ingrese su apellido ")
pais = input("Ingrese el país en el que vive ")
edad = input("Ingrese su edad ")
