#Ingresar tres números y representarlos gráficamente, ordenados de mayor a menor en forma horizontal


n1= int(input("ingrese un el numero 1:")),
n2= int(input("ingrese un el numero 2:")),
n3= int(input("ingrese un el numero 3:")),

if ((n1 <= n2) and (n1 <= n3)):
    menor=n1,
    if(n2<=n3):
        medio=n2,
        mayor=n3,
    else:
        medio=n3,
        mayor=n2,
elif((n2<=n1) and (n2 < n3 )):
    menor=n2,
    if(n1<=n3):
        medio=n1,
        mayor=n3,
    else:
        medio=n3,
        mayor=n1
else:
    menor=n3,
    if(n1<=n2):
        medio=n1,
        mayor=n2,
    else:
        medio=n2,
        mayor= n1,
print(str (mayor) , str(medio) , str(menor)),