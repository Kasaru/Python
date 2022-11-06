a,b,c = input(), input(), input()
if len(a) == min(len(a), len(b), len(c)) and len(b) == max(len(a), len(b), len(c)):
    print(a)
    print(b)
elif len(a) == min(len(a), len(b), len(c)) and len(c) == max(len(a), len(b), len(c)):
    print(a)
    print(c)
elif len(b) == min(len(a), len(b), len(c)) and len(a) == max(len(a), len(b), len(c)):
    print(b)
    print(a)
elif len(c) == min(len(a), len(b), len(c)) and len(b) == max(len(a), len(b), len(c)):
    print(c)
    print(b)
else:
    print(c)
    print(a)