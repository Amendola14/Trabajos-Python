#1.Ingresar dias, horas, minutos y segundos mostrar los segundos totales

Dias_Seg = 86400
Horas_Seg =3600
min_seg =60

days = int(input('Ingresar la cantidad de dias: '))
hours = int(input('Ingresar la cantidad de horas: '))
minutes = int(input('Ingresar la cantidad de minutos: '))
seconds = int(input('Ingresar la cantidad de segundos: '))

totalSeconds = (days * Dias_Seg) + (hours * Horas_Seg) + (minutes * min_seg) + seconds
