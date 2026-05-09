#taking total amount as input from user
Amount =int(input("Pleas Enter amount for withdraw :"))

#Calculating the numberof notes of different denominations
note_1 = Amount//1000
note_2 = (Amount%1000)//100
note_3 =  ((Amount%1000)%100)//50


print("note of 1000 shillings" , note_1)
print("notes of 100 shillings ", note_2)
print("notes of 50 shillings" , note_3)