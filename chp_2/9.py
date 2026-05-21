#Add 2 list values as per their position value. For example - 
#L1 = [1, 2, 3]
#L2 = [4, 5, 6]
#L3 = [5, 7, 9]
l1=[1,2,3]
l2=[4,5,6]
l3=[]
for i in range(len(l1)):
    l3.append(l1[i]+l2[i])

print(l3)