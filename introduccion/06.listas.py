#Contenedor de datos...
nombres = ["aaron","alan"]

#Las matrices son listas dentro de otras listas
matrices = [[0,3],[0,2]]

#Se pueden tener listas con distintos tipos de datos, tambien
listaRandom = ["aaron",27,["Argentina"]]

#Para acceder al valor en una lista, tenemos que acceder a su posición
#Accediendo al nombre de listaRandom
print(listaRandom[0])

#Accediendo al nombre de Argentina
print(listaRandom[2][0])

#Concatenar dos lista en una
listasJuntas = listaRandom + nombres
print(listasJuntas)

#Hacer una lista del 1 hasta 8(no incluido)
lista = list(range(1,8))
print(lista)