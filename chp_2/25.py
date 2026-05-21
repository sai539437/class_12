##odd even program #main-accepts number from user count the number respectively and take their sum out 
def odd_even(n):
    sum_even = 0
    sum_odd = 0
    for i in range(n+1):
        if i%2==0:
            sum_even=sum_even+i
        else:
            sum_odd=sum_odd+i
    print(sum_even,sum_odd)

n=int(input("enter the number you want"))
odd_even(n)