a,b = int(input()),int(input())
y=0
for i in range(a,b+1):
    if (i**3)%10==4 or (i**3)%10==9:
        y+=1
print(y)