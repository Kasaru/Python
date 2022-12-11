a = int(input())
for i in range(1,a+1):
    divider = 0
    for j in range(i,0,-1):
        if i % j == 0:
            divider += 1
    print(i,divider*"+",sep="")