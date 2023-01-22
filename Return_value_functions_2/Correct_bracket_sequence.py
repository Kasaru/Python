# объявление функции
def is_correct_bracket(text):
    count = 0
    for i in range(len(text)):
        if text[i] == "(":
            count += 1
        elif text[i] == ")":
            count -= 1
            if count < 0:
                return False
    if count == 0:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))