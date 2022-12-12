s = input()
count = 0
for i in range(len(s)):
    if s[i] == s.lower()[i] and s[i] not in "1234567890":
        count += 1
print(count)