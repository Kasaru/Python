s = input()
Max = 0
s2 = ''
for i in range(len(s)):
    if s.count(s[i]) >= Max:
        s2 = s[i]
        Max = s.count(s[i])
print(s2)