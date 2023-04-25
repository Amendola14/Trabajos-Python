#Determinar si un año ingresado por teclado es o no bisiesto

año=int(input("ingrerse un año y le diremos su es bisiesto o no: "))

if año % 4 !=0: 
    print("el año",año," no es bisiesto")
elif año % 4 == 0 and año % 100 != 0: #divisible entre 4 y no entre 100 o 400
	print("Es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: #divisible entre 4 y 10 y no entre 400
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: #divisible entre 4, 100 y 400
	print("Es bisiesto")