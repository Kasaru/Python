punctuation = ',./\|!@#$%^&*(){}[]";:'
en_lower_alph = 'abcdefghijklmnopqrstuvwxyz'
en_upper_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text = input()
mess = []
enc = ''
mess += text.split(' ')
w = 0
for i in range(len(mess)):
    c = 0
    for j in range(len(mess[i])):
        if mess[i][j] not in punctuation:
            c +=1
    for k in range(len(mess[w])):
        if mess[w][k].isupper() and mess[w][k] in en_upper_alph:
            enc += en_upper_alph[(en_upper_alph.index(mess[w][k]) + c)%len(en_upper_alph)]
        elif mess[w][k].islower() and mess[w][k] in en_lower_alph:
            enc += en_lower_alph[(en_lower_alph.index(mess[i][k]) + c)%len(en_lower_alph)]
        else:
            enc += mess[w][k]
    w += 1
    if w < len(mess):
        enc += ' '
print(enc)