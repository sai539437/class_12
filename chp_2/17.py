#Design a function that prints an order summary for an online cart. Pass item names, quantities, and prices as keyword arguments.
def onlinecard(item,name,quantities,prices):
    return(item,name,quantities,prices)
item=int(input("enter the number of items you want"))
name=input("enter the name of product")
q=int(input("enter the the number of quantites"))
price=int(input("enter the price"))
print(item,name,q,price)
