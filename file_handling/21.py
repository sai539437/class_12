#Write a function that receives two string arguments and checks whether they are same-length strings (returns True in this case otherwise False).
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2):
    print(True)
else:
    print(False)