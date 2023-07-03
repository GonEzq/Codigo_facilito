nombre = 'Gonzalo'
apellido = 'rivera'

nombre_completo = nombre + ' ' + apellido

print(nombre_completo)

# ----------------------------------------------------

nombre = 'Gonzalo'
apellido = 'rivera'

nombre_completo_2 = 'Mr. %s %s %s.' %(nombre, apellido, 'luna')

print(nombre_completo_2)

# ----------------------------------------------------------

nombre = 'Gonzalo'
apellido = 'rivera'

nombre_completo_3 = 'Mr. {} {}.'.format(nombre, apellido)

print(nombre_completo_3)


nombre_completo_4 = f'Mr. {nombre} {apellido} {"Rivera"} {1.9} {10 * 8}'
print(nombre_completo_4)