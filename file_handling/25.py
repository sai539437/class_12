#wap that takes a number n and then return a randomly genrated number having exactly a digits not starting with zero eg 
#if n is 2 then returns a randomly generated number having exactly n digit (not starting with zero)if n is 2 then function can randomly return a number 
#10-99but 07,02 etc.are not valid two digit 

import random 
def ran(val):
    lst = []
    for i in range(val):
        value = random.randint(1,9)
        lst.append(value)
    print(lst)

val = int(input('Enter the number of digits to generate value : '))
ran(val)