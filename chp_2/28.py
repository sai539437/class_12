#Write a function add_contact() that accepts a phone_book, name, and number.
#  Add the entry if the name doesn't exist; otherwise, print "Contact already exists".
def add_contact(phone_book):
    name = input("Enter your name: ")
    num = input("Enter your number: ")
    if name in phone_book:
        print("Contact already exists")
    else:
        phone_book[name] = num
        print("Contact added successfully")
phone_book = {}
n = int(input("no of contacts you want to add"))
for i in range(n):
    add_contact(phone_book)
print( phone_book)
    

