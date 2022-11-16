a,b = int(input()),int(input())
for i in range(a,b+1):
    if i%17==0 or i%10==9 or (i%3==0 and i%5==0):
        print(i)