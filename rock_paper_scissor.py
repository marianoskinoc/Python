import random

options = ("scissor", "rock", "paper")

print("welcome to rock, paper, scissor ")
user_option = input("what is option selected?\n").lower()

if not user_option in options:
  print("that option does not exist ")
  
computer_option = random.choice(options)

if user_option == computer_option:
  print("Computer option is", computer_option)
  print("Tie!")
  
elif user_option == "rock":
  if computer_option == "scissor":
    print("Computer option is", computer_option)
    print("you win, rock beats scissor")
  else:
    print("Computer option is", computer_option)
    print("you losse, paper beats rock")
elif user_option == "paper":
  if computer_option == "rock":
    print("Computer option is", computer_option)
    print("you win, paper beats rock")
  else:
    print("Computer option is", computer_option)
    print("you losse, scissor beats paper")
elif user_option == "scissor":
  if computer_option == "paper":
    print("Computer option is", computer_option)
    print("you win, sccisor beats paper")
  else:
    print("Computer option is", computer_option)
    print("you losse, rock beats scissor")
    