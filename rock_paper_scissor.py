import random

print("Bienvenido a piedra papel o tijera")

options = ("piedra", "papel","tijera")

win_human = 0
win_machine = 0
round = 1


while win_human < 3 and win_machine < 3:
    
    print("*" * 15)
    print("Ronda", round)
    user_option = input("Cual es su elección => ").lower()

    if not user_option in options:
        print("la opción ingresada no es correcta")
        continue
    computer_option = random.choice(options)
    

    if user_option == computer_option:
        print("Empate")

    elif user_option == "tijera":
        if computer_option == "papel":
            print("Usted gana tijera corta papel")
            win_human += 1
            print("tu =",win_human, "\nmaquina" , win_machine)
        else:
            print("usted pierde piedra rompe tijeras")
            win_machine += 1
            print("tu =",win_human, "\nmaquina" , win_machine)
    elif user_option == "papel":
        if computer_option == "piedra":
            print("Usted gana papel envuelve piedra")
            win_human += 1
            print("tu =",win_human, "\nmaquina" , win_machine)
        else:
            print("usted pierde tijera corta papel")
            win_machine += 1
            print("tu =",win_human, "\nmaquina" , win_machine)
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("Usted gana piedra rompe tijera")
            win_human += 1
            print("tu =",win_human, "\nmaquina" , win_machine)
        else:
            print("usted pierde tijera corta papel")
            win_machine += 1
            print("tu =",win_human, "\nmaquina" , win_machine)
    round += 1