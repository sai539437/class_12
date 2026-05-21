# Write a function that receives two numbers and generates a random number from that range. Using this function, 
# the main program should be able to print three numbers randomly 
import random
a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))
print("Random numbers are:")
print(random.randint(a, b))
print(random.randint(a, b))
print(random.randint(a, b))