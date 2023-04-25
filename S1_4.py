#4.Convertir una distancia en Km a metros, pulgadas, yardas y millas.#
Kilomentros=1
Metro=1000
pulgadas=39370.1
Yardas= 1093,61
millas=0.621371


kilometros = int(input('Ingresar la cantidad en kilometros: '))

Yardas= kilometros * Yardas
millas= kilometros * millas
pulgadas= kilometros * pulgadas
Metro= kilometros * Metro

print(kilometros, "la cantidad ingresada en Kilometros en Yardas Son: ", Yardas)
print(kilometros, "la cantidad ingresada en Kilometros en millas Son: ", millas)
print(kilometros, "la cantidad ingresada en Kilometros en pulgadas Son: ", pulgadas)
print(kilometros, "la cantidad ingresada en Kilometros en Metro Son: ", Metro)