s = input()
if len(s) % 2 == 0:
    if s[:len(s)//2:1] == s[:-len(s)//2-1:-1]:
        print("YES")
    else:
        print("NO")
else:
    if s[:len(s)//2:1] == s[:-len(s)//2:-1]:
        print("YES")
    else:
        print("NO")