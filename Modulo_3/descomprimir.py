uno, dos, tres, cuatro = 1, 2, 3, 4

print(uno)
print(dos)
print(tres)
print(cuatro)

# tambien se puede realizar con dupla (mas corto)
# * -> lista
# _ -> Omitir valor
numeros = (1, 2, 3, 4, 5)
uno, dos, tres, *resto_valores = numeros


print(uno)
print(dos)
print(tres)
print(cuatro)
print(resto_valores)
#tambien se puede realizar de la siguiente forma. 

numeros = ( 1, 2, 3, 4 )
uno = numeros [0]
dos = numeros [1]
tres = numeros [2]
cuatro = numeros [3]

print(uno)
print(dos)
print(tres)
print(cuatro)

