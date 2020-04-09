seguir = 'si'

while seguir == 'si':

	nombre = input('digite palabra\n')
	palindromo = nombre[::-1]

	if palindromo == nombre:
		print(nombre, 'es palindromo\n')
	else:
		print(nombre, 'no es un palindromo\n')
	seguir = input('si para continuar\n')