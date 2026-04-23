### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_other_tuple = (20, 56, 34, 27, 32)

my_tuple = (35, 1.57, "Keyla", "Diaz", "Keyla")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Keyla"))
print(my_tuple.index("Keyla"))
print(my_tuple.index("Diaz"))

# La tupla es inmutable
# my_tuple[1] = 1.80 Typerror 'tuple' object does not support item assignment
# print(my_tuple) 

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Argentina"
my_tuple.insert(1, "Black")
print(my_tuple)
my_tuple = tuple(my_tuple)
print(type(my_tuple))

del my_tuple #  elimina la variable
# print(my_tuple) NameError: name 'my_tuple' is not defined
