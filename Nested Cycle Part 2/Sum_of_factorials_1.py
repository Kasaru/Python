n = int(input())
Sum = 0
factorial = 1
for i in range(1,n+1):
    for j in range(i,0,-1):
        factorial *= j
    Sum += factorial
    factorial = 1
print(Sum)