lenguajes = 'python ruby java rust c++ C'

listado_lenguajes = lenguajes.split() #

print(listado_lenguajes)


lenguajes_2 = 'python-ruby-java-rust-c++-C'

listado_lenguajes_2 = lenguajes_2.split('-') # su puede poner en el argunmento con dividiriamos.

print(listado_lenguajes_2)


lenguajes_3 = 'python-ruby-java-rust-c++-C'

listado_lenguajes_3 = lenguajes_3.split('-', 2) # el sundo argumento es para saltar. 

print(listado_lenguajes_3)


lenguajes_4 = ['python', 'ruby', 'java', 'rust', 'c++', 'C']

string_lenguajes_4 = '-'.join(lenguajes_4)
print(string_lenguajes_4)
