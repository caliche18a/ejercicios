"""
Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura
(en metros), calcule el índice de masa corporal y lo almacene en
una variable, y muestre por pantalla la frase Tu índice de masa
corporal es <imc> donde <imc> es el índice de masa corporal calculado
redondeado con dos decimales.
Fórlula de IMC: peso/(estatura)**2
"""
peso = float(input("Ingrese su peso: "))
estatura = float(input("Ingrese su estatura: "))

imc = peso / (estatura)**2
imc = round(imc,2)

print("Su índice de masa corporal es: "+str(imc))