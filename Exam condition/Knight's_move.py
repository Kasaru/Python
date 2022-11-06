a,b,c,d = int(input()),int(input()),int(input()),int(input())
if (c==a+2 and d==b+1) or (c==a-2 and d==b+1) or (c==a+2 and d==b-1) or (c==a-2 and d==b-1) or (c==a+1 and d==b+2) or (c==a-1 and d==b+2) or (c==a+1 and d==b-2) or (c==a-1 and d==b-2):
    print("YES")
else:
    print("NO")