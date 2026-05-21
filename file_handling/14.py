#wap a program that creates a list of integers less than 100 that are mutiples of of 3 or 5 
my_list=[] 
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        my_list.append(i)
print(my_list)