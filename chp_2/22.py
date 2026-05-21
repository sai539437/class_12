#main 
#x=10,print(id(x)test(x)
def test(x):
    print(id(x))
global x
x=10
print(id(x))
test(x)
x=20
print(id(x))