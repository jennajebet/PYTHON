secret= 34
attempts = 5

for i in range(attempts):
    guess = int(input("Guess a number between (1-50): "))

 if guess==secret:
  print("You won hurray!!🎊")
  break
  
 elif abs (secret - guess) <=3:
  print("🔥almost there!")

 elif abs(secret- guess)<=10:
   print("Close but not yet!")

 else:
  print("Ohh no a bit far")

hearts=" "
remaining = attempts - i - 1

count = 0
while count < remaining:
   hearts +="❤️"
   count += 1
print("remaining guesses:", "❤️", hearts )

else:
  print("Womp womp you lost the game! The secret number was,", secret)
