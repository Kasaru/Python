def get_factors(num):
    l = []
    for i in range(1,num + 1):
        if num % i == 0:
            l+= [i]
    return l
# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))