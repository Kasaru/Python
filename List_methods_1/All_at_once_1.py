numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
fl = 0
print(len(numbers))#Вывел длину списка;
print(numbers[len(numbers)-1])#Вывел последний элемент списка;
print(numbers[len(numbers)::-1])#Вывел список в обратном порядке (вспоминаем срезы);
for i in range(len(numbers)):#Вывел YES если список содержит числа 5 и 17, и NO в противном случае;
    if numbers[i] == 5:
        fl = 1
    if numbers[i] == 7 and fl == 1:
        fl = 2
if fl == 2:
    print("YES")
else:
    print("NO")
del numbers[0]
del numbers[len(numbers)-1]
print(numbers) #Вывел список с удаленным первым и последним элементами.