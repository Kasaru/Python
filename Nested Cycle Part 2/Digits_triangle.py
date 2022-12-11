n = 5
k = 0
for i in range(1,n+1):
    for j in range(1,i+1):
        print(k+j, end = ' ')
    print()
    k += i