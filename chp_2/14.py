#Write a function that takes a person's name as an argument and prints a greeting message with the name.
# The function should have a default greeting message if none is provided
def greet(name,greeting="hello"):
    print(f"{greeting}, {name}!")

name=input("enter your name")
g=input("enter your greeting")
print(name)
print(g)
greet(name,g)


