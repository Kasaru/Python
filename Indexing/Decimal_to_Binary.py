n = int(input())
binar = ""
while n != 0:
    if n % 2 == 0:
        binar += str(n % 2)
    else:
        binar += "1"
    n //= 2
for i in range(len(binar)-1,-1,-1):
    print(binar[i], end = "")