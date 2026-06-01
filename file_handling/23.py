#Write a program that generates a series using a function which takes first and last
# values of the series and then generates four terms that are equidistant e.g., if two numbers passed are 1 and 7 then function returns 1 3 5 7.
# Function to generate 4 equidistant terms

def series(first,last):
    difference=(last-first)//3
    print(first,first+difference,first+2*difference,last)
a=int(input("enter the first number"))
b=int(input("enter the second number"))
series(a,b)
