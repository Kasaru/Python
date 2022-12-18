n = int(input())
l = []
for i in range(n):
    d = int(input())
    l += [d]
print(*l, sep = "\n")
print()
for i in l:
    print((i * i) + 2 * i + 1)