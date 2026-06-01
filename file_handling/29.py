#create a mass conversion.py that stores a function for mass conversion eg 
#kgtotonne() to kg to tonnes #kg to pound() to convert kg to pund tonnetokg() to convert tonne to kg pound to kg() to convert pound to kg 
#1kg=0.001 tonne 1kg=2.20462 
def kgtotonne(kg):
    tonnes = kg * 0.001
    return tonnes
def kgtopound(kg):
    pound = kg * 2.20462
    return pound
def tonnetokg(tg):
    kg = tg * 1000
    return kg
def poundtokg(pound):
    kg = pound / 2.20462
    return kg
kg = int(input("Enter kilograms: "))
print("Tonnes =", kgtotonne(kg))
print("Pounds =", kgtopound(kg))

tg = float(input("Enter tonnes: "))
print("Kilograms =", tonnetokg(tg))

pound = float(input("Enter pounds: "))
print("Kilograms =", poundtokg(pound))