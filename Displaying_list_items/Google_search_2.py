n = int(input())
l1,l2 = [],[]
for i in range(n):
    s = input()
    l1 += [s]
k = int(input())
for i in range(k):
    r = input()
    l2 += [r]
for i in range(len(l1)):
    count = 0
    for j in range(len(l2)):
        if l2[j].lower() in l1[i].lower():
            count += 1
            if count == k:
                print(l1[i])