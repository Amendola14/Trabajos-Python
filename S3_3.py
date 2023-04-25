#Hacer un conversor de temperaturas que funcione con °C, K, y °F

unid_tem= input("ingrese unidad de temperatura: ")
temperatura=int(input("ingrese la temperatura: "))

if unid_tem.lower() =="c":
    k=273.15 + temperatura
    f=((9/5) + temperatura) + 32
    print(f"{temperatura} C- {f} F- {k} K")
elif unid_tem.lower()== "F":
    pass
else:
    pass