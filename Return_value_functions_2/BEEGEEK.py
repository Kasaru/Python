def is_valid_password(password):
    l = password.split(":")
    count = 0
    for i in range(0, int(len(l[0]) / 2)): # палиндром
        if l[0][i] != l[0][len(l[0]) - i - 1]:
            return False
    for i in range(1,int(l[1]) + 1): # простое
        if int(l[1]) % i == 0:
            count += 1
        if count > 2:
            break
    if count != 2:
        return False
    if int(l[2]) % 2 != 0: # четное
        return False
    if len(l) != 3:
        return False
    return True

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))