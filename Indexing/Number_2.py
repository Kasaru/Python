s = input()
fl = 0
for i in range(len(s)):
    if s[i] in "0123456789":
        fl = 1
        break
if fl == 1:
    print("Цифра")
else:
    print("Цифр нет")