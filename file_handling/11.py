#wap that takes two lines L and M of the same size and adds their elements together to form a new list N 
#Whose elements are sum of the corresponding elements in L AND M L=[3,1,4] AND M=[1,5,9] AND N=[4,6,13]
l = [3, 1, 4]
m = [1, 5, 9]
n = []
for i in range(len(l)):
    total = l[i] + m[i]
    n.append(total)

print(n)