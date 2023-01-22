def get_days(month):
    if month % 2 == 0 and month != 2 and month < 8:
        return 30
    elif month % 2 != 0 and month > 8:
        return 30
    elif month == 2:
        return 28
    else:
        return 31

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))