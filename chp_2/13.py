#convert  a celcius and frahenite using def function 
def celcuis(c):
    return(c*9/5)+32
def frahenite(f):
    return(f-32)*5/9
c=int(input("enter the value in celcius:"))
f=int(input("enter the value in frahenite:"))
s1=frahenite(f)
s2=celcuis(c)
print(s1,"is the value in celcuis")
print(s2,"is the value in frahenite")

# main()


