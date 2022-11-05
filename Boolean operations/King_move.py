a,b,c,d = int(input()),int(input()),int(input()),int(input())
if (c==a and d==b+1) or (c==a+1 and d==b) or (c==a+1 and d==b+1) or (c==a-1 and d==b) or (c==a and d==b-1) or (c==a-1 and d==b-1) or (c==a-1 and d==b+1) or (c==a+1 and d==b-1):
    print("YES")
else:
    print("NO")