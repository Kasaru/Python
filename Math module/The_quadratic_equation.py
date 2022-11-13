import math
a,b,c = float(input()),float(input()),float(input())
if b**2-4*a*c == 0:
    print(-b/(2*a))
elif b**2-4*a*c > 0:
    if ((-b-math.sqrt(b**2-4*a*c))/(2*a))<((-b+math.sqrt(b**2-4*a*c))/(2*a)):
        print((-b-math.sqrt(b**2-4*a*c))/(2*a))
        print((-b+math.sqrt(b**2-4*a*c))/(2*a))
    else:
        print((-b+math.sqrt(b**2-4*a*c))/(2*a))
        print((-b-math.sqrt(b**2-4*a*c))/(2*a))
else:
    print("Нет корней")