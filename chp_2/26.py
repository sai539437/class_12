# ask user to enter marks of all the subjects and calculate the total marks in function - stu_marks and show total marks
def stu_marks(marks):
    total_marks=sum(marks)
    print(total_marks)
    s1=int(input("enter your english marks"))
    s2=int(input("enter your maths marks"))
    s3=int(input("enter your phy marks"))
    s4=int(input("enter your chem marks"))
    total_marks=(s1+s2+s3+s4)
    print(total_marks)
    

