#write a program to search value in dictionary and print its key#class 11
dict={"name:john","age:25","city:new york"}
value=input("enter the value to search:")
for item in dict:
    key,value=item.split(":")
    if value==value:
        print("key:",key)
        break
    else:
        print("value not available in dictionary")
        