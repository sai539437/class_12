#write a program to search value in dictionary and print its key 
r=input("enter the value to find its key:")
d={"sai":1,"vishal":2,}
for key,value in d.items():
    if value==r:
        print(key)