import math
n = int(input())
Sum = 0
for i in range(1,n+1):
    Sum += math.factorial(i)
print(Sum)