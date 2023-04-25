#Hacer un programa que simule un dado. El valor del dado debe ser aleatorio.
import random

def lanzar_dado():
    return random.randint(1, 6)

resultado = lanzar_dado()
print(f"El dado ha caído en {resultado}")