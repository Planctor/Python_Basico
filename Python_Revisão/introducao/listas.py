lista_numeros = [50,5,9,7,92,21,6,841,9,5]
lista_letras = ["a", "b", "c","d"]
matriz = [[1,2,3],[4,5,6],[7,8,9]]

lista_numeros.append(24)
lista_numeros.reverse()

print(lista_numeros)
print(lista_numeros.index(5))
print(lista_numeros.count(5))
lista_numeros.sort()
lista_numeros.extend(lista_letras)
lista_letras_dois =  lista_numeros.copy().extend(lista_letras)
print(lista_letras_dois)
print(lista_numeros)
print(matriz)
