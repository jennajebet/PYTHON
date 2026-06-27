import random
playing=True
number=str(random.randint(0,9))

print("i will generate a number from 0 to 9 and you have to guess the number one digit at a time")

while playing:
    guess=input("Give me your best guess! \n")
    if number == guess:
        print("You win the game!")
        print("The number was:", number)
        break

    else:
        print("Your guess isnt quite right, trye again\n")