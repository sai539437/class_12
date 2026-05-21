
#Design a modular Python program to manage a shopping cart. Requirements:
#1. Separate functions for: Validation (qty/price > 0), Subtotal, Discount (10% if > ₹1000), GST (18%), and Invoice display.
#2. a main order_summary(**items) that orchestrates the flow.
#3. Final output must include item-wise details, Subtotal, Discount, GST, and Final amount.
#4. Function must return a dictionary with all calculated values.""""""

def  order_summary(item):
    return(order_summary)
quantity=int(input("enter the number of quantity of item"))
name=input("enter the name of the product")
price=int(input("enter the price of the product"))
total_cost=(quantity+price)
print("the number of quantity of your item is",quantity)
print("the name of the product",name)
print(price)
if price>1000:
    dicount=price*0.1
    print("you get a discount of 10%")
    gst=price*0.18
    print("you have to pay gst of 18%")
else:
    if price<=1000:
        print("you do not get any discount")
        gst=price*0.18
        print("you have to pay a gst of 18%")
        total_cost=quantity*price+gst
        print(total_cost)
print(quantity,name,price,total_cost)


        



