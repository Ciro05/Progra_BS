conjunto_a = {4, 12, 51, 21, 77}
conjunto_b = {5, 13, 34, 21, 42}


#Agregando un elemento nuevo
conjunto_a.add(6)
print(conjunto_a)

#Agregando un elemento duplicado
conjunto_a.add(4)
print(conjunto_a)  

#Eliminando un elemento del conjunto
conjunto_a.remove(4)
print(conjunto_a)  

#Uniendo dos conjuntos
union = conjunto_a | conjunto_b
print(union)

#intersección de conjuntos
interseccion = conjunto_a & conjunto_b
print(interseccion)

#diferencia de conjuntos
diferencia = conjunto_a - conjunto_b
print(diferencia)

#verificar si existe elemento
print(3 in conjunto_a)