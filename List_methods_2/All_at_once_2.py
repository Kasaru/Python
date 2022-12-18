numbers = [8, 9, 10, 11]
del numbers[1]#Заменил второй элемент списка на 17;
numbers.insert(1,17)
numbers.append(4)#Добавил числа 4, 5 и 6 в конец списка;
numbers.append(5)
numbers.append(6)
del numbers[0]#Удалил первый элемент списка;
numbers.extend(numbers)#Удвоил список;
numbers.insert(3,25)#Вставил число 25 по индексу 3;
print(numbers)#Вывел список, с помощью функции print()