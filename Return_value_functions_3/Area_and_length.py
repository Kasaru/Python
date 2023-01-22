# объявление функции
import math
def get_circle(radius):
    c = 2 * math.pi * radius
    s = math.pi * radius ** 2
    return c,s

# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)