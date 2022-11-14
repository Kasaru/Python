m,p,n = int(input()),int(input()),int(input())
for i in range(n):
    if i == 0:
        print(i+1, m)
    else:
        m = 0.01 * p * m + m
        print(i+1, m)