print("""yoo guys let's play rock,paper,scissors""")
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

import random
user_choice=int(input('enter your choices: 1."ROCK", 2."PAPER",3."SCISSORS":'))
opponent=random.randint(1,3)
print(f"computer choice: {opponent}")
if user_choice>=4:
    print("invalid number")
elif user_choice==1 and opponent==2:
    print("you lose")
elif user_choice==2 and opponent==3:
    print("you lose")
elif user_choice==3 and opponent==1:
    print("you lose")
elif user_choice==opponent:
    print("it's a draw")
else:
    print("you win")
