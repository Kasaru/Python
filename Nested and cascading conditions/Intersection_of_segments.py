a,b,c,d = int(input()),int(input()),int(input()),int(input())
if a<=c<b and b<d:
    print(c,b)
elif b==c:
    print(c)
elif a<d<b and c<=a:
    print(a,d)
elif (a<=c<b and a<d<=b)or(a==c and b==d):
    print(c,d)
elif (c<=a<d and c<b<=d):
    print(a,b)
elif d==a or (d==b and c<a<b):
    print(d)
else:
    print("пустое множество")