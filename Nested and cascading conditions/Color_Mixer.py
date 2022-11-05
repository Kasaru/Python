a,b = input(), input()
if a==b and a in ("красный","синий","желтый"):
    print(a)
elif (a == "красный" and b == "синий")or(a == "синий" and b == "красный"):
    print("фиолетовый")
elif (a == "красный" and b == "желтый")or(a =="желтый" and b == "красный"):
    print("оранжевый")   
elif (a == "синий" and b == "желтый")or(a == "желтый" and b == "синий"):
    print("зеленый")  
else:
    print("ошибка цвета")