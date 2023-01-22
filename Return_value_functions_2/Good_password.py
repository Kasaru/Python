def is_password_good(password):
    l = list(password)
    fl = True
    a,b,c,d = 0,0,0,0
    if len(l) >= 8 :
        a = 1
    for i in range(len(l)):
        if l[i].isdigit():
            b = 1
        elif l[i].isupper():
            c = 1
        elif l[i].islower():
            d = 1
    if a + b + c + d == 4:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))