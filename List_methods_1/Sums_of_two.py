n = int(input())
d1,d2 = 0,0
l = []
for i in range(1,n + 1):
    d = int(input())
    if i % 2 != 0:
        d1 = d
    else:
        d2 = d
    if i >=2:
        l += [d1 + d2]
print(l)