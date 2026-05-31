print("Half Pyramid pattern of exclamation marks(!):")
n= int(input("Enter the numberof rows:"))
for i in range(n):
    for j in range(i+1):
        print("!", end="")
    print()