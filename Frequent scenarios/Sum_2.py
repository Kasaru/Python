a = int(input())
g = 0
for i in range(1,a+1):
    if ((i**2)%10==2)or((i**2)%10==5)or((i**2)%10==2):
        g+=i
print(g)
