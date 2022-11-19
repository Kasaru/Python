y=0
for i in range(1,11):
    n = int(input())
    if n%2!=0:
        print("NO")
        break
    else:
        y+=1
if y == 10:
    print("YES")