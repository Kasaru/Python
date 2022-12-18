l = input().split('.')
fl = 0
for i in range(len(l)):
    if int(l[i]) > 255:
        fl = 1
if fl == 0:
    print("ДА")
else:
    print("НЕТ")