s = 'abcdefghijklmnopqrstuvwxyz'
l = []
for i in range(len(s)):
    if s[i] == 'a':
        l += [1 * s[i]]
    else:
        l += [(i+1) * s[i]]
print(l)