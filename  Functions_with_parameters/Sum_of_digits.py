def print_digit_sum(num):
    Sum = 0
    for i in range(len(num)):
        Sum += int(num[i])
    print(Sum)


# считываем данные
n = input()

# вызываем функцию
print_digit_sum(n)