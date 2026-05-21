#wap that rotates the element of a list so that the element at the first idex moves to the second index the element in the 
#second index moves to the third index etc and moves the elemnt in the last index moves to the first index 

lst = [10, 20, 30]
print(lst)

temp = lst[0]
lst[1]=lst[0]
lst[0]=lst[2]
lst[2]=temp

print(lst)
