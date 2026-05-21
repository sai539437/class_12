#Program which accept a 10 digit phone number and responds in formatted manner if correct number entered by user 010 - 123 - 456 - 7890
n=input("enter the 10 digit phone number:")
if len(n)==10:
    print("-",n[6:10], "-",n[0:3],"-",n[2:4])
else:
    print("invalid number")
    