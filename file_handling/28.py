#create a module lenght conversion.py that stores the functions for various lenght conversion eg 
#miletokm(),convert miles to kilometer #kmtomile()-convert km to miles #feettoinches() #inchestofeet()

def miletokm(m):
    km=m*1.609
    return km
def kmtomile(k):
    m=k / 1.609
    return k 
def feettoinches(f):
    inches=f*12
    return f 
def inchesfeet(i):
    ft=i/12
    return i

miles=int(input("enter the number of miles"))
print("km =",miletokm(miles))
km=int(input("enter km"))
print("m=",kmtomile(km))
feet = int(input("Enter feet: "))
print("Inches =", feettoinches(feet))
feet = int(input("Enter feet: "))
print("Inches =", feettoinches(feet))





