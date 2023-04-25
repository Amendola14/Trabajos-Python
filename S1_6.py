#Hacer un programa que permita mostrar un ticket de devolución de envases para un supermercado.#
Precio_Botella_De_Vidrio=1.50
Precio_Botella_De_Plástica=2

Botella_De_Vidrio=int(input("ingrese cantidad de Botellas De Vidrio: " ))
Botella_De_Plástica=int(input("ingrese cantidad de Botellas De PLatico: " ))

cantidad_de_botellas= Botella_De_Vidrio + Botella_De_Plástica

total_de_valor_de_botellas_de_Vidrio = Botella_De_Vidrio * Precio_Botella_De_Vidrio

total_valor_de_botellas_de_Plastico= Botella_De_Plástica * Precio_Botella_De_Plástica

valor_Total=total_de_valor_de_botellas_de_Vidrio + total_valor_de_botellas_de_Plastico



ticket = f"""
Ingrese botellas:
vidrio: \t{Botella_De_Vidrio}
plástico: \t{Botella_De_Plástica}
Devolución de botellas
========================
plástico {Botella_De_Plástica} \t{total_valor_de_botellas_de_Plastico}
vidrio {Botella_De_Vidrio} \t{total_valor_de_botellas_de_Plastico}
------------------------
total {cantidad_de_botellas} \t{valor_Total}
"""

print(ticket)