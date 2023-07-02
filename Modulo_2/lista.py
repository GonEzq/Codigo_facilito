# comienza en el indice 0 en adelante. 
#                   0         1         2        3       4   
#                   -5        -4        -3       -2      -1

#lista_cursos = [ 'python', 'django', 'flask', 'Ruby', 'Java'] #list()

#primer_curso = lista_cursos [0]

#print (primer_curso)


#segundo_curso = lista_cursos [-4]

#print (segundo_curso)

# reemplazar

#lista_cursos = [ 'python', 'django', 'flask', 'Ruby', 'Java'] #list()

#lista_cursos[4] = 'Rust'
#print(lista_cursos)


#sublista

#lista_cursos = [ 'python', 'django', 'flask', 'Ruby', 'Java', 'Rust'] #list()

#para genera un sub lista [star:end] no se toma en cuenta el ultimo indice (end)
# [start:] optenemos los ultimos elementos de la lista. 
#sub_lista = lista_cursos[0:3]
#print(sub_lista)


#[:end] obtenemos los primeros elementos de la lista
#lista_cursos = [ 'python', 'django', 'flask', 'Ruby', 'Java', 'Rust'] #list()
#sub_lista = lista_cursos[:4]
#print(sub_lista)

#[start:end:skip] realizo salto en la lista
#sub_lista = lista_cursos [1:5:2]
#print(sub_lista)


#lista_cursos = [ 'python', 'django', 'flask', 'Ruby', 'Java', 'Rust'] #list()
#lista_curso_2 = ['C', 'C++', 'Docker']
#print (len(lista_cursos))

#lista_cursos.append('MongoDB') #nos permite añadir un elemto al final de la lista
#lista_cursos.insert(1,'Rails') # nos permite añadir un elemento segun la posicion que le pongamos al indice

#lista_cursos.extend(lista_curso_2) #es para unir o exter la lista con otra lista. 

#print(lista_cursos)
#print (len(lista_cursos))

#lista_cursos.remove('MongoDB') #para elimiar un elemeto de una lista

#print(lista_cursos)

#del lista_cursos[0] # para eleminar un elemento de una lista con la palabra reservada del y el indice.

#print(lista_cursos)

#lista_cursos.clear() # eliminar los elementos de la lista, todo los elementos. 
#print(len(lista_cursos))

#ordenar la listas. sort ()

lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

#lista.sort(reverse=True)

#print (lista)

#lista.sort()
#print(lista [1]) # min
#print(lista [2]) # max 

#lista_2 = [8, 90, 1, 5, 44, 132, 600, 3, 4]
#lista_2.sort()

#print( min (lista_2))
#print( max (lista_2))

#para encontrar un valor en la lista.
print(10 in lista)

print( 5 in lista)

index = lista.index(5)
print(index)