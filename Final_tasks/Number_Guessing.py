from random import *
import sys
def is_valid(s,n1,n2):
    return s.isdigit() and n1 <= int(s) <= n2
def new_game(s,n1,n2):
    while s not in '+-':
        print("Прости, не понял, сыграем еще раз?(+\-)")
        s = input()
    if s == '+':
        changes()
        game(n1,n2)
    if s == '-':
        sys.exit("Ну ты это, заходи если что!")

def game(n1,n2):
    n = randint(n1, n2)
    print(f"Число в диапазоне [{n1},{n2}] загадано, введите ваше число:")
    answer = input()
    сount = 1
    while not is_valid(answer,n1,n2):
        print(f"Введенное значение не является числом или оно вне диапазона [{n1},{n2}], попробуйте снова:")
        answer = input()
        is_valid(answer,n1,n2)
    while n != int(answer):
        if n < int(answer):
            print("Слишком много, попробуй еще раз:")
            answer = input()
            while not is_valid(answer, n1, n2):
                print(f"Введенное значение не является числом или оно вне диапазона [{n1},{n2}], попробуйте снова:")
                answer = input()
                is_valid(answer, n1, n2)
            сount += 1
        elif n > int(answer) and is_valid(answer,n1,n2):
            print("Слишком мало, попробуй еще раз:")
            answer = input()
            while not is_valid(answer, n1, n2):
                print(f"Введенное значение не является числом или оно вне диапазона [{n1},{n2}], попробуйте снова:")
                answer = input()
                is_valid(answer, n1, n2)
            сount += 1
    print(f"Поздравляю, ты угадал!!! \nКоличество попыток: {сount} \nВерное число:{n}")
    print(f"Начать новую игру? (+\-)")
    answer = input()
    gc = 1
    new_game(answer,n1,n2)
def changes():
    print("Хочешь сменить диапазон чисел?(+\-)")
    answer = input()
    while answer not in '+-':
        print("Прости, не понял, будем меня диапазон?(+\-)")
        answer = input()
    if answer == '+':
        print("Введи новое начальное число диапазона:")
        n1 = check_changes1(input())
        print("Введи новое конечное число диапазона:")
        n2 = check_changes2(n1)
        game(n1, n2)
def check_changes1(s):
        while not valid_digit(s):
            print(f"Введенное значение не является числом, попробуйте снова:")
            s = input()
            valid_digit(s)
        return int(s)
def check_changes2(n1):
    s = input()
    while not valid_digit(s):
        print(f"Введенное значение не является числом, попробуйте снова:")
        s = input()
        valid_digit(s)
    while int(s) <= int(n1):
        print("Конечное число должно быть больше начального, попробуй еще раз:")
        s = input()
        while not valid_digit(s):
            print(f"Введенное значение не является числом, попробуй снова:")
            s = input()
            valid_digit(s)
    return int(s)
def valid_digit(s):
    return s.isdigit()
gc = 0
n1 = 1
n2 = 100
if gc == 0:
    print("Добро пожаловать в числовую угадайку")
    game(n1,n2)
else:
    game(n1,n2)