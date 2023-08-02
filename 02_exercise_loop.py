"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""
age = int(input("Escriba su edad\n"))
print("*"*30)

year = 2023

for i in range(age+1):
    print("cumpliste ",age ,"en el año", year)
    year -= 1
    age -= 1
    if age == 0:
        print("naciste en", year)
        break