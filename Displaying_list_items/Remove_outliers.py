n = int(input())
l = []
for i in range(n):
    d = int(input())
    l += [d]
del l[l.index(max(l))]
del l[l.index(min(l))]
print(*l, sep = '\n')