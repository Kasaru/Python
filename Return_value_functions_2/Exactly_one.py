# объявление функции
def is_one_away(word1, word2):
    l1 = list(word1)
    l2 = list(word2)
    same = 0
    for i in range(len(word1)):
        if l1[i] == l2[i]:
            same += 1
    if same == len(l1) - 1:
        return True
    else:
        return False
# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))