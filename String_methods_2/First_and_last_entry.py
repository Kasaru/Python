import math
s = input()
i1,i2 = math.pi,math.pi + 1
for i in range(len(s)):
    if s[i] == "f" and i1 == math.pi:
        i1 = i
    elif s[i] == "f" and i1 != math.pi:
        i2 = i
if i1 == math.pi:
    print("NO")
elif i2 == math.pi +1:
    print(i1)
else:
    print(i1,i2)