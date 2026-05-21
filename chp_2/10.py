#Add 2 list values as per their position value. For example - 
#L1 = [[1, 2, 3],[4, 5, 6]]
#L2 = [[4, 5, 6],[7, 8, 9]]
#L3 = Add both list values into L3

l1=[[1,2,3],[4, 5, 6]]
l2 = [[4, 5, 6],[7, 8, 9]]
l3=[]
for i in range(len(l1)):
    l3.append(l1[i]+l2[i])
print(l3)
