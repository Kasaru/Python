n = int(input())
max1 = 0
max2 = 0
for i in range(1,n+1):
    a = int(input())
    if a>max1:
        max2=max1
        max1=a
    elif max1>a>max2:
        max2=a
print(max1)
print(max2)