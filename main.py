import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choices = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if user_choice >= 0 and user_choice < 3:

  print("User Choice")
  print(choices[user_choice])

  computer_choice = random.randint(0, 2)
  print("Computer Choice")
  print(choices[computer_choice])



  if user_choice == 0 and computer_choice == 2:
    print("You wins!")
  elif computer_choice == 0 and user_choice == 2:
    print("Computer wins! You lose!")
  elif user_choice == computer_choice:
    print("It's draw.")
  elif user_choice > computer_choice:
    print("You wins!")
  elif computer_choice > user_choice:
    print("Computer wins! You lose!")
else:
  print("You input is invalid. You lose!")