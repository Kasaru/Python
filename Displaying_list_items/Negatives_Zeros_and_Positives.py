n = int(input())
l1,l2,l3 = [],[],[]
for i in range(n):
    d = int(input())
    l1 += [d]
for i in range(len(l1)):
    if l1[i] < 0:
        print(l1[i])
    elif l1[i] == 0:
        l2.append(l1[i])
    else:
        l3.append(l1[i])
print(*l2, *l3,sep = '\n')