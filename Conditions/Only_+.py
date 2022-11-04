a,b,c = int(input()), int(input()), int(input())
if a>=0 and b>=0 and c>=0:
    print(a+b+c)
elif a<0 and b>=0 and c>=0:
    print(b+c)
elif a>=0 and b<0 and c>=0:
    print(a+c)
elif a>=0 and b>=0 and c<0:
    print(a+b)
elif a<0 and b<0 and c>=0:
    print(c)
elif a<0 and b>=0 and c<0:
    print(b)
elif a>=0 and b<0 and c<0:
    print(a)
else:
    print(0)