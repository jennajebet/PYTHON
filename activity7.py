buying_price = float(input("Enter the actual cost of the item : "))

selling_price = float(input("Enter the selling price of the item:"))

if(buying_price > selling_price):
    loss = buying_price - selling_price
    print("you incurred a loss of:", loss)
else:
    profit= selling_price - buying_price
    print("you made a profit of :", profit)