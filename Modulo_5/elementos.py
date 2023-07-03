diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print ('a' in diccionario)

valor = diccionario ['d']

print(valor)



# get

valor_1 = diccionario.get ('z')
print(valor_1)

#setdefault

valor_2 = diccionario.setdefault('e', 5)

print(valor_2)
print(diccionario)