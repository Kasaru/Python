n = int(input())
l = []
for i in range(n):
    d = int(input())
    l += [d]
del l[1::2]
print(l)