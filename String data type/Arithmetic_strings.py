a,b,c = input(), input(), input()
if (len(a)-len(b)==len(b)-len(c)) or (len(b)-len(a)==len(a)-len(c)) or (len(c)-len(a)==len(a)-len(b)) or (len(a)-len(c)==len(c)-len(b)):
    print("YES")
else:
    print("NO")