n = int(input())
s = input()
for i in range(len(s)):
    if ord(s[i]) - 96 - n > 0:
        print(chr(ord(s[i]) - n), end = "")
    else:
        print(chr(122 + (ord(s[i]) - 96 - n)), end = "")