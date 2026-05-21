#Write a program that generates a series using a function which takes first and last 

# values of the series and then generates four terms that are equidistant e.g., if two numbers passed are 1 and 7 then function returns 1 3 5 7.
# Function to generate 4 equidistant terms
def series(a, b):
    step = (b - a) // 3   

    print("Series ")
    print(a)
    print(a + step)
    print(a + 2 * step)
    print(b)
a = int(input("Enter first number: "))
b = int(input("Enter last number: "))
series(a, b)