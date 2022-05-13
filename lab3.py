# Ejercicio 1
myString = "Soy un string"
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
print(myString, "is of the data type", str(type(myString)))

# Ejercicio 2
firstString = "water"
secondString = "fall"
thirdString = firstString+secondString
print(thirdString)

# Ejercicio 3
name = input("What is your name?\n")
print(name)

# Ejercicio 4
color = input("¿Cuál es tu color favorito?\n")
animal = input("¿Cuál es tu animal favorito?\n")

print("{}, le gusta un {} {}".format(name, color, animal))