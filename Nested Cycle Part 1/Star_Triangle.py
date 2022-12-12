n = int(input())
count = 0
for i in range(1,n):
    if i <= n // 2:
        for j in range(i,i+1):
            print(j*"*")
            count += 1
    elif count != n:
        for k in range(i,0,-1):
            print(k*"*")
            count +=1
            if count == n:
                break