def is_palindrome(text):
    l = []
    text = text.lower()
    for i in range(len(text)):
        if text[i] not in '.,!?- ':
            l += text[i]
    for i in range(0, int(len(l) / 2)):
        if l[i] != l[len(l) - i - 1]:
            return False
    return True

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))