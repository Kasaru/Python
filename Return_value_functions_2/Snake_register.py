# объявление функции
def convert_to_python_case(text):
    l = list(text)
    s = ''
    for i in range(len(l)-1):
        if l[i].isupper() and i !=0:
            l[i] = l[i].lower()
            l.insert(i,'_')
        if i == 0:
            l[i] = l[i].lower()
    s = s.join(l)
    return s

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))