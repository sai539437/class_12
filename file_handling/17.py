#wap a function that takes amount in dollar and dollor to rupee conversation price it then return the amount converted to rupees create the function 
#in both void and in void forms 
#menu driver
# menu driven currency converter

def dollar_to_rupee():
    dollar = int(input("Enter amount in Dollar: "))
    rate = int(input("Enter conversion rate (1 Dollar = ? Rupees): "))

    rupee = dollar * rate
    print("Amount in Rupees =", rupee)


def rupee_to_dollar():
    rupee = int(input("Enter amount in Rupees: "))
    rate = int(input("Enter conversion rate (1 Dollar = ? Rupees): "))

    dollar = rupee / rate
    print("Amount in Dollars =", dollar)


while True:
    print("\nCurrency Converter")
    print("1. Dollar to Rupee")
    print("2. Rupee to Dollar")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        dollar_to_rupee()

    elif choice == 2:
        rupee_to_dollar()

    elif choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")

    