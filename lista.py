nombres = ["Ciro", "Alan", "Kendra", "Alejandro"]

numeros = [1, 12, 10, 33, 510]

mixta = [7, "Programación", False, 2.34]

#Imprimiendo solo los primeros tres numeros
dos_primeros= numeros[:3]
print(dos_primeros) 

sin_los_tres_primeros = numeros[3:]
print(sin_los_tres_primeros) 

#Para imprimir valores mediante indices
print(nombres[-1])  

#Para cambiar valores de la listamediante indices
numeros[3] = 232
print(numeros)  

#Eliminar valores de la lista por indices
valor_eliminado = numeros.pop(1)
print(valor_eliminado)  
print(numeros)  

#Eliminar valores de la lista con el metodo remove
nombres.remove("Alan")
print(nombres)  

#Combinando listas
lista_combinada = numeros + nombres
print(lista_combinada)  

largo = len(numeros)
print(largo)

