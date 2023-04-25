#2. Realizar el procedimiento inverso al 1: Mostrar cuántos días, horas, minutos y segundos representa una cantidad de segundos ingresados por consola.

DIas_segundos= 86400
Horas_segundos =3600
Minutos_segundos =60

totalSeconds = int(input('Ingresar la cantidad en segundos: '))

days = totalSeconds // DIas_segundos
hours = (totalSeconds - (days * DIas_segundos) )// Horas_segundos
minutes = (totalSeconds - (hours * Horas_segundos) - (days * DIas_segundos)) // Minutos_segundos
seconds = (totalSeconds - (minutes * Minutos_segundos) - (hours * Horas_segundos) - (days * DIas_segundos))

print('La cantidad de Dias es:', days,'la cantidad de Horas es:', hours,'la cantidad de Minutos:', minutes,'la cantidad de Segundos:', seconds)