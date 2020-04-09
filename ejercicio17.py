import datetime

fechaactual = datetime.datetime.now()
print('Fecha actual', fechaactual.date())

fechanaci = input('Digite su fecha de nacimiento (aaaa-mm-dd)\n')
fechanacimiento = datetime.datetime.strptime(fechanaci, '%Y-%m-%d')
print('Fecha nacimiento:', fechanacimiento.date())

diferencia = fechaactual - fechanacimiento
print('Entre las 2 fechas hay:', diferencia.days, 'dias')