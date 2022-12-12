s = input()
if len(s) % 2 == 0:
    print(s[len(s) // 2 : len(s)], s[ : len(s) // 2], sep = "")
else:
    print(s[len(s) // 2 + 1 : len(s)], s[ 0: len(s) // 2 + 1], sep = "")