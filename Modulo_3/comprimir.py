lista = [1, 2, 3, 4, 5]

tupla = (10, 20, 30, 40, 50)

lista_2 = [100, 200, 300, 400, 500]

resultado = zip (lista_2, tupla, lista) # -> zip

resultado = tuple (resultado)

print(resultado)