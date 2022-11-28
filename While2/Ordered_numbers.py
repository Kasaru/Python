n = int(input())
LEN = len(str(n))
count=1
while n%10 <= (n//10)%10:
    count += 1
    n = n//10
if LEN == count:
    print("YES")
else:
    print("NO")