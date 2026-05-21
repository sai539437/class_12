

#
#function 
def counter_increment():
    global increment
    print(increment)
    increment=increment+1

#main
increment=0
counter_increment()
print(increment)
