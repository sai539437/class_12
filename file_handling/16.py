#fibonacci series tuple storing first 9 terms 
fib = [0, 1]
for i in range(7): 
    fib.append(fib[-1] + fib[-2])
fibonacci_tuple = tuple(fib)
print(fibonacci_tuple)

