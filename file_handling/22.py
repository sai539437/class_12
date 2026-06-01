# Write a function that takes two numbers and returns the number that has minimum one's digit.
#  [For example, if numbers passed are 491 and 278, then the function will return 491 because it has got minimum one's digit
#  out of two given numbers (491's 1 is < 278's 8)].
def min_o_d(n1, n2):
    if n1 % 10 < n2 % 10:
        return n1
    else:
        return n2

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print( min_o_d(n1, n2))