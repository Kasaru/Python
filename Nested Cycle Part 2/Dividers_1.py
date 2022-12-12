a,b = int(input()), int(input())
digit = 0
Sum = 0
MaxSum = 0
for i in range(a,b+1):
    Sum = 0
    for j in range(i,0,-1):
        if i % j == 0:
            Sum += j
        if Sum >= MaxSum:
            MaxSum = Sum
            digit = i
print(digit, MaxSum)