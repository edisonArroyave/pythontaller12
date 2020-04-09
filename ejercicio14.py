cadena = input('Escriba un texto\n')
cadena = cadena.lower()
contador = 0

for cad in cadena:
  if cad in "aeiou":
    contador += 1

print('Cadena: ',cadena)
print('Cantidad de vocales:', contador)