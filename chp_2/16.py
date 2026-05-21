#create a function that displays student information like name,age and grade use keyword argument to call the function 
def students(name,grade,age):
    return(name,grade,age)
name=input("enter your name")
grade=int(input("enter your grade"))
age=int(input("enter your age"))
print(name,grade,age)