"""
Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas
trabajadas y el coste por hora. Después debe mostrar por
pantalla la paga que le corresponde.
"""
horasTrabajadas = int(input("Ingrese el número de horas trabajadas: "))
costoHora = float(input("Ingrese el costo de la hora: "))
pago = horasTrabajadas * costoHora
print("El pago correspondiente por sus "+str(horasTrabajadas)+" horas es $"+str(pago))