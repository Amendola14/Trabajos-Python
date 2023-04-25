#Informe la cantidad de días en un mes (se ingresa mes y año por teclado)

import calendar

mes = int(input("Ingrese el número del mes (1-12): "))
año = int(input("Ingrese el año: "))


dias_en_el_mes = calendar.monthrange(año, mes)[1]

print(f" El mes {mes} del año {año}: ")
