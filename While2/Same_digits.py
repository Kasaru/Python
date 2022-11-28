n = 11111
LEN = len(str(n))
count = 1
while n%10 == (n//10)%10:
    n = n//10
    count += 1
if count == LEN:
    print("YES")
else:
    print("NO")