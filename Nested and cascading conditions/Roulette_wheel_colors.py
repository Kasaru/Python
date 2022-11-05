a = int(input())
if (1<=a<=10 and a%2==0)or(19<=a<=28 and a%2==0)or(11<=a<=18 and a%2!=0)or(29<=a<=36 and a%2!=0):
    print("черный")
elif (1<=a<=10 and a%2!=0)or(19<=a<=28 and a%2!=0)or(11<=a<=18 and a%2==0)or(29<=a<=36 and a%2==0):
    print("красный")
elif a == 0:
    print("зеленый")
else:
    print("ошибка ввода")