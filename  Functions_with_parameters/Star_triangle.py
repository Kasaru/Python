def draw_triangle(fill, base):
    for i in range(1,base+1):
        if i <= (base + 1) // 2:
            print(i * fill)
        else:
            print((base - i + 1) * fill)

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)