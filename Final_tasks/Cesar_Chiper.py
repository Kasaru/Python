def greetings():
    print('Вас приветствует программа шифр Цезаря, желаете зашифровать encr, или расшифровать decr?')
    answer = valid_answer()
    print('Выберите язык текста ru или en')
    lang = valid_lang()
    if answer == 'encr':
        print('Какое смещение использовать?')
        ROH = input()
        print('Какой текст зашифровать?')
        Text = input()
        if lang == 'ru':
            encrypt_ru(ROH,Text,enc)
        elif lang == 'en':
            encrupt_en(ROH,Text,enc)
    elif answer == 'decr':
        print('Известно ли, какое смещение было использовано? (+\-)')
        ans = valid_answer2()
        if ans == '+':
            print('Какое смещение было использовано?')
            ROH = input()
            print('Введите зашифрованый текст?')
            Text = input()
            if lang == 'ru':
                decrypt_ru(ROH, Text, enc)
            elif lang == 'en':
                decrypt_en(ROH, Text, enc)
        else:
            print('Введите зашифрованый текст?')
            Text = input()
            brut_ROH(Text,enc)

def encrypt_ru(ROH,Text,enc):
    for i in Text:
        if i.isupper() and i in ru_upper_alph:
            enc += ru_upper_alph[(ru_upper_alph.index(i) + int(ROH))%len(ru_upper_alph)]
        elif i.islower() and i in ru_lower_alph:
            enc += ru_lower_alph[(ru_lower_alph.index(i) + int(ROH))%len(ru_lower_alph)]
        else:
            enc += i
    print(f'Выбранный текст зашифрован со смещением: {ROH} \nЗашифрованный текст: {enc}')

def decrypt_ru(ROH,Text,enc):
    for i in Text:
        if i.isupper() and i in ru_upper_alph:
            enc += ru_upper_alph[(ru_upper_alph.index(i) - int(ROH))%len(ru_upper_alph)]
        elif i.islower() and i in ru_lower_alph:
            enc += ru_lower_alph[(ru_lower_alph.index(i) - int(ROH))%len(ru_lower_alph)]
        else:
            enc += i
    print(f'Выбранный текст был зашифрован со смещением: {ROH} \nРасшифрованный текст: {enc}')
def encrupt_en(ROH,Text,enc):
    for i in Text:
        if i.isupper() and i in en_upper_alph:
            enc += en_upper_alph[(en_upper_alph.index(i) + int(ROH))%len(en_upper_alph)]
        elif i.islower() and i in en_lower_alph:
            enc += en_lower_alph[(en_lower_alph.index(i) + int(ROH))%len(en_lower_alph)]
        else:
            enc += i
    print(f'Выбранный текст зашифрован со смещением: {ROH} \nЗашифрованный текст: {enc}')
def decrypt_en(ROH,Text,enc):
    for i in Text:
        if i.isupper() and i in en_upper_alph:
            enc += en_upper_alph[(en_upper_alph.index(i) - int(ROH))%len(en_upper_alph)]
        elif i.islower() and i in en_lower_alph:
            enc += en_lower_alph[(en_lower_alph.index(i) - int(ROH))%len(en_lower_alph)]
        else:
            enc += i
    print(f'Выбранный текст был зашифрован со смещением: {ROH} \nРасшифрованный текст: {enc}')
def brut_ROH(Text,enc):
    for j in range(0,len(en_lower_alph)):
        enc = ''
        for i in Text:
            if i.isupper() and i in en_upper_alph:
                enc += en_upper_alph[(en_upper_alph.index(i) - j) % len(en_upper_alph)]
            elif i.islower() and i in en_lower_alph:
                enc += en_lower_alph[(en_lower_alph.index(i) - j) % len(en_lower_alph)]
            else:
                enc += i
        print(f'Выбранный текст был зашифрован со смещением: {j} \nРасшифрованный текст: {enc}')
def valid_answer():
    l = {'encr','decr'}
    answer = input()
    while answer not in l or answer == '':
        print('Некорректный ответ, введите encr для шифрования или decr для дешифрования')
        answer = input()
    return answer
def valid_answer2():
    answer = input()
    while answer not in '+-' or answer == '':
        print('Некорректный ответ, введите + = Да или - = Нет')
        answer = input()
    return answer
def valid_lang():
    l = {'ru', 'en'}
    lang = input()
    while lang not in l or lang == '':
        print('Некорректный ответ, введите encr для шифрования или decr для дешифрования')
        lang = input()
    return lang

ru_lower_alph = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
ru_upper_alph = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
en_lower_alph = 'abcdefghijklmnopqrstuvwxyz'
en_upper_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ROH = 0
enc = ''
decr = ''
greetings()