n = int(input())
l = []
for i in range(n):
    s = input()
    if s not in l:
        l += [s]
print(*l, sep = "\n")