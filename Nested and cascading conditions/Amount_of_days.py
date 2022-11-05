a = int(input())
if (a%2!=0 and a!=2 and a<8) or a==8 or (a>8 and a%2==0):
    print(31)
elif a == 2:
    print(28)
else:
    print(30)