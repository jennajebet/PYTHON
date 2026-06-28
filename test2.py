def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b ==0:
        return "Error Cannot divide by 0(Zero)."
    return a/b

print("1.Add")
print("2.Subtract")
print("3.Divide")
print("4.Multiply")

pick = input("Choose an operation from (1-4):")

try:
    num1= float(input("Enter your first number:"))
    num2= float(input("Enter your second number:"))

    if pick =="1":
        print("Answer:",  add(num1, num2))

    elif pick=="2":
        print("Answer:", subtract(num1, num2))

    elif pick=="3":
        print("Answer:", divide(num1, num2))

    elif pick=="4":
        print("Answer:", multiply(num1, num2))

    else:
        print("Woops wrong operation!")

except ValueError  :
    print("Error, enter valid numbers")  