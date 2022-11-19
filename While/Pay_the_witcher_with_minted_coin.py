n = int(input())
count = 0
while n != 0:
    if n>=25:
        n-=25
        count+=1
    elif 25>n>=10:
        n-=10
        count+=1
    elif 10>n>=5:
        n-=5
        count+=1
    elif 5>n>=1:
        n-=1
        count+=1
print(count)