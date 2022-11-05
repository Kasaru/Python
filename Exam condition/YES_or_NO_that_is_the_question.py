a = int(input())
if a%2!=0 or (a%2==0 and 6<=a<=20):
    print("YES")
elif (a%2==0 and 2<=a<=5) or (a%2==0 and a>20):
    print("NO")