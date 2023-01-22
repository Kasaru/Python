# объявление функции
def get_middle_point(x1, y1, x2, y2):
    x = (x2+x1)/2
    y = (y2+y1)/2
    return x,y

# считываем данные
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

# вызываем функцию
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)