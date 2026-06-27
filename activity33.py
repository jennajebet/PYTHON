import random

options=["Rock", "Paper", "Scissors"]

users_choice= input("Choose rock, paper os scissors:")

computers_choice=random.choice(options)

print("You choose:", users_choice)
print("computers_choice:",computers_choice)

if users_choice == computers_choice:
    print("It is a tie!")

elif users_choice== "Rock" and computers_choice== "Scissors":
    print("Rock smashes paper, you win!")

elif users_choice== "Paper" and computers_choice== "Rock":
    print("Paper covers rock, you win!")

elif users_choice== "Scissors" and computers_choice== "Paper":
    print("Scissors cuts paper, you win!")

else:
    print("You lose!")

