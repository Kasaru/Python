s = input()
s2 = ''
for i in range(s.find('h'),s.rfind('h')+1):
    s2 += s[i]
s = s.replace(s2,'')
print(s)