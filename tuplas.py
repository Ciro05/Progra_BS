tupla = (44, 57, 3, 91, 64, 34, 3)

#imprimir elementos de la tupla
print(tupla[0])  

#creando unasubtupla
sub_tupla = tupla[1:4]
print(sub_tupla) 

#concatenando tuplas
tupla_concatenada = tupla + (6, 7, 8)
print(tupla_concatenada)

#duplicando elementos de la tupla
tupla_repetida = tupla * 2
print(tupla_repetida) 

#tamaño de la tupla
longitud = len(tupla)
print(longitud)  

#cuantas veces aparece un elemento en la tupla
contador = tupla.count(3)
print(contador)