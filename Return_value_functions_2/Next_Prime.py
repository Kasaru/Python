def is_prime(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
            if count > 2:
                break
    if count == 2:
        return True
    else:
        return False
def get_next_prime(num):
    n = num
    r = False
    while r == False:
        n += 1
        r = is_prime(n)
    return n


# считываем данные
n = int(input())
# вызываем функцию
print(get_next_prime(n))