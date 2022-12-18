n = int(input())
l1 = []
for i in range(n):
    s = input()
    l1 += [s]
k = int(input())
for i in range(len(l1)):
    if len(l1[i]) >= k:
        print(l1[i][k-1],end = '')