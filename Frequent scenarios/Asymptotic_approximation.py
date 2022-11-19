import math
a = int(input())
g = 1
for i in range(2,a+1):
    g+=1/i
print(g-math.log(a))