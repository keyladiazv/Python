# Operadores Aritmeticos

print(3 + 4)    # Suma
print(3 - 4)    # Resta
print(3 * 4)    # Multiplicación
print(3 / 4)    # División
print(10 % 2)   # Módulo
print(10 // 3)  # División de piso
print(10 ** 3)  # Exponencial

print(10 ** 3 + 3 - 7 / 1 // 4)

# Concatenación de String
print("Hola" + "Python" + "¿Qué tal?")
print("Hola " + str(5))
print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

# Operadores Comparativos
print(3 > 4)    # Mayor 
print(3 < 4)    # Menor
print(4 >= 4)   # Mayor o igual 
print(3 <= 4)   # Menor o igual
print(3 == 4)   # Igual
print(3 != 4)   # Distinto
print( 3 > 4 == 2)
print ( 3 > 4 > 2)

print("Hola" > "Python")    
print("Hola" < "Python")    
print("aaaa" >= "abaa")   # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaaa"))   # Cuenta caracteres
print("Hola" == "Hola")     
print("Hola" != "Python")   


# Operadores Lógicos
print(3 > 4 and "Hola" > "Python")  # False y False = False
print(3 > 4 or "Hola" > "Python")   # False o False = False
print(3 < 4 and "Hola" < "Python")  # True y True = True
print(3 < 4 or "Hola" > "Python")   # True o False = True
print(3 < 4 or ("Hola" > "Python" and 4 == 4)) # True o (False y True) = True o False = True
print(not(3 > 4)) # Para negar toda la condición

"""
Tabla de verdad
and
True and True = True
True and False = False
False and False = False
False and True = False
or
True or True = True
True or False = True
False or False = False
False or True = True
"""