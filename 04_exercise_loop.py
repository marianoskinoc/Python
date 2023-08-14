"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre 
por pantalla el capital obtenido en la inversión cada año que dura la inversión."""

principal = int(input("Ingrese el monton a invertir\n"))
tasa_interes = int(input("Interes anual\n"))
años = int(input("Tiempo a dejar en años\n"))

tasa_interes = tasa_interes * 0.01
ganancia_total = 0

for i in range(1,años+1):
    
    print("*"*30)
    
    ganancia_anual = principal * tasa_interes
    ganancia_total += ganancia_anual
    principal += ganancia_anual
    ganancia_total_formatted = "{:.2f}".format(ganancia_total)
    print("El interes generado en",i,"es",ganancia_total_formatted)