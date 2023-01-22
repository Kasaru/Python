import random
def greetings(chars):
    chars += digits
    print('Вас приветствует генератор безопасных паролей, какое количество паролей необходимо создать?')
    n = input()
    n = valid_digit(n)
    print(f'Будет сгенерировано {n} паролей, какой длинны должен быть пароль?(минимум 8 символов)')
    l = input()
    l = valid_digit(l)
    while int(l) < 8:
        print('Пароль слишком короткий, пожалуйста ведите корректное значение, не менее 8')
        l = input()
        l = valid_digit(l)
    print('Включать ли заглавные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (+/-)')
    answer = input()
    valid_answer(answer)
    if answer == '+':
        chars += uppercase_letters
    print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (+/-)')
    answer = input()
    valid_answer(answer)
    if answer == '+':
        chars += lowercase_letters
    print('Включать ли символы !#$%&*+-=?@^_? (+/-)')
    answer = input()
    valid_answer(answer)
    if answer == '+':
        chars += punctuation
    print('Исключать ли неоднозначные символы il1Lo0O? (+/-)')
    answer = input()
    valid_answer(answer)
    if answer == '+':
        for i in exclude:
            chars = chars.replace(i,'')
    for i in range(int(n)):
        generate_password(chars,l)
def generate_password(chars,l):
        password = ''
        while len(password) != l:
            symbol = random.choice(chars)
            password += symbol
        print(password)
def valid_answer(answer):
    while answer not in '+-' or answer == '':
        print('Некорректный ответ, введите + = Да или - = Нет')
        answer = input()
def valid_digit(s):
    while not s.isdigit():
        print('Некорректный ответ, введите любое число:')
        s = input()
    return int(s)

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exclude = 'il1Lo0O'
symbol = ''
chars = ''
password = ''
greetings(chars)