rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

ROCK
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

PAPER
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

SCISSORS
'''

#Write your code below this line 👇
import random

player = int(input("What do you choose? (0 for Rock, 1 for Paper, 2 for Scissors): "))
RPS = [rock, paper, scissors]
opp_choice = random.choice(RPS)

print(RPS[player])
print(" vs.")
print(opp_choice)

if player == 0:
  if opp_choice == rock:
    print("TIE")
  elif opp_choice == paper:
    print("You Lose")
  elif opp_choice == scissors:
    print("You Win")
elif player == 1:
  if opp_choice == rock:
    print("You Win")
  elif opp_choice == paper:
    print("TIE")
  elif opp_choice == scissors:
    print("You Lose")
else:
  if opp_choice == rock:
    print("You Lose")
  elif opp_choice == paper:
    print("You Win")
  elif opp_choice == scissors:
    print("Tie")