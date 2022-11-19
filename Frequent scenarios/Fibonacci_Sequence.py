fib1 = fib2 = 1
n = int(input())
if n == 1:
    print(fib1, end=" ")
else:
    print(fib1,fib2, sep=" ", end=" ")
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')