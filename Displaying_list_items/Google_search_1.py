n = int(input())
l = []
for i in range(n):
    s = input()
    l += [s]
r = input()
for i in range(len(l)):
    if r.lower() in l[i].lower():
        print(l[i])