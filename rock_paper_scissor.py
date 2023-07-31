import random

options = ("scissor", "rock", "papper")

print("welcome to rock, papper, scissor ")
user_option = input("what is option selected?\n").lower()

if not user_option in options:
  print("that option does not exist ")
computer_option = random.choice(options)

if user_option == computer_option:
  print("Computer option is", computer_option)
  print("empat!")
  
elif user_option == "rock":
  if computer_option == "scissor":
    print("Computer option is", computer_option)
    print("you win, rock beats scissor")
  else:
    print("Computer option is", computer_option)
    print("you losse, papper beats rock")
elif user_option == "papper":
  if computer_option == "rock":
    print("Computer option is", computer_option)
    print("you win, papper beats rock")
  else:
    print("Computer option is", computer_option)
    print("you losse, scissor beats papper")
elif user_option == "scissor":
  if computer_option == "papper":
    print("Computer option is", computer_option)
    print("you win, sccisor beats papper")
  else:
    print("Computer option is", computer_option)
    print("you losse, rock beats scissor")
    