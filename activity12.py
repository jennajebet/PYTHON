print("select your ride")
print("1. Bike")
print("2. Car")

choice= int(input("Enter your choice:"))

if choice==1:
    print("What type of bike? ")
    print("1. scooty\n")
    print("2. scooter\n")

    choice_2= int(input("Enter your choice:"))
    if choice_2==1:
        print("You have selected a scooty")
    else:
        print("You have selected a scooter")

elif(choice ==2):
    print("What type of car?")
    print("1.sedan\n")
    print("2.hatchback\n")

    choice_3= int(input("Enter your choice..."))
    if choice_3==1:
        print("You have selected a sedan")
    else:
        print("You have selected a hatchback")
else:
    print("wrong choice")
