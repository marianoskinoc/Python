"""Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces."""
word = input("Ingrese una palabra\n")
print("-"*30)
for i in range(0,10):
    print(i,"-",word)