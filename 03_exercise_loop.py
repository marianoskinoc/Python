"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas."""

number = int(input("Ingrese un numero entero positivo\n"))
list_impar = []
if number > 0 :
    for i in range (1,number+1):
        if not i % 2 == 0:
            i = str(i)
            list_impar.append(i)
            
            
else:
    print("Vuelva a ejecutar el programa e ingrese lo solicitado")

result = ",".join(list_impar)
print(result)
