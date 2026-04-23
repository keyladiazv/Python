"""
1.  Escribe un ejemplo para diferentes tipos de datos de Python, 
    como Number (entero, flotante, complejo), 
    String, Boolean, List, Tuple, Set y Dictionary.
"""
# Number
entero = 10         # int
flotante = 3.14     # float
complejo = 2 + 3j   # complex

print("Entero: ", entero)
print("Flotante: ", flotante)
print("Complejo: ", complejo)

# String
texto = "Hola, Python"
print("String: ", texto)

# Boolean
verdadero = True
falso = False

print("Boolean True: ", verdadero)
print("Boolean False: ", falso)

# List (mutable)
lista = [1, 2, 3, "Hola"]
print("Lista: ", lista)

# Tuple (inmutable)
tupla = (10, 20, 30, "Hola")
print("Tupla: ", tupla)

# Set (sin elementos repetidos)
conjunto = {1, 2, 3, 4, 5}
print("Set: ", conjunto)

# Dictionary (clave : valor)
diccionario = {
    "nombre" : "Keyla",
    "edad" : 32,
    "profesión" : "Criminologo"
}
print("Diccionario: ", diccionario)

"""
2. Calcula la distancia euclidiana entre (2, 3) y (10, 8).
    Formula 
    distancia = abs(p - q)
"""

# Distancia euclidiana entre (2, 3)
p = 2
q = 3
distancia = abs(p - q)
print("La distancia euclidiana entre (2, 3) es de: ", distancia)

# Distancia euclidiana entre (10, 8)
p = 10
q = 8
distancia = abs(p - q)
print("La distancia euclidiana entre (10, 8) es de: ", distancia)