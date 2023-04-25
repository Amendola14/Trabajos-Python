#8.Escribir un programa que muestre la suma de los n primeros números enteros entre 1 y n (n lo ingresan por teclado)


print('Escribir un programa que muestre la suma de los N primeros números enteros entre 1 y N (N lo ingresan por teclado)')

N = int(input('Ingresar numero: '))

value = (N * (N + 1))//2

print(f'La suma de los números entre 1 y {N} es',value)