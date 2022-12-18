n = input()
n = int(n.strip("#"))
for i in range(n):
    l = input()
    if "#" in l:
        l = l[:l.index("#")]
        print(l.rstrip())
    else:
        print(l.rstrip())