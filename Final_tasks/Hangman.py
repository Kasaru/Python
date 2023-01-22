from random import *
word_list = ["человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок", "история", "женщина", "развитие", "власть", "правительство", "начальник", "спектакль", "автомобиль", "экономика", "литература", "граница", "магазин", "председатель", "сотрудник", "республика", "личность"]
def get_word():
    word = randint(0, len(word_list) - 1)
    game(word_list[word].upper())
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |    // \\\\
                   |    \\\\ //
                   |     / \\
                   |    /   \\
                   |     
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |    // \\\\
                   |    \\\\ //
                   |     / 
                   |    /   
                   |     
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |    // \\\\
                   |    \\\\ //
                   |      
                   |       
                   |     
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |    // \\
                   |    \\\\ /
                   |      
                   |       
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |     / \\
                   |     \ /
                   |      
                   |       
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |     
                   |     
                   |      
                   |       
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |     
                   |     
                   |      
                   |       
                   |     
                   -
                ''',
    ]
    print(stages[tries])
def game(word):
    print("Welcome to Hangman! \nLet's play!")
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False       # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []    # список уже названных слов
    tries = 6             # количество попыток
    while not guessed and tries > 0:
        display_hangman(tries)
        print(word_completion)
        print('Введите слово или букву:')
        answer = valid_answer(guessed_letters,guessed_words)
        if len(answer) == 1 and answer in word:
            guessed_letters += answer
            letters = list(word_completion)
            for i in range(len(word)):
                if word[i] == answer and letters[i] == '_':
                    letters[i] = answer
            word_completion = ''.join(letters)
            if word_completion == word:
                guessed = True
        elif len(answer) > 1 and answer == word:
            guessed = True
        elif len(answer) > 1 and answer != word:
            tries -= 1
            guessed_words += answer.split(' ')
        elif len(answer) == 1 and answer not in word:
            tries -= 1
            guessed_letters += answer
    if guessed and tries > 0:
        print('Поздравляем, вы угадали слово! Вы победили!\nЖелаете сыграть снова?')
        answer = valid_answer2()
        new_game(answer)
    if not guessed and tries == 0:
        print(f'Вы проиграли \nЗагаданное слово: {word}\nЖелаете сыграть снова?')
        answer = valid_answer2()
        new_game(answer)
def valid_answer(guessed_letters,guessed_words):
    answer = input().upper()
    while not answer.isalpha():
        print('Некорректный ответ, введите одну букву или одно слово')
        answer = input().upper()
    while answer in guessed_letters and len(answer) == 1:
        print(f'Буква уже использовалась, введите любую букву или слово кроме {guessed_letters}')
        answer = input().upper()
    while answer in guessed_words and len(answer) > 1:
        print(f'Буква уже использовалась, введите любую букву или слово кроме {guessed_words}')
        answer = input().upper()
    return answer.upper()
def valid_answer2():
    answer = input()
    while answer not in '+-' or answer == '':
        print('Некорректный ответ, введите + = Да или - = Нет')
        answer = input()
    return answer
def new_game(answer):
    if answer == '+':
        get_word()
    elif answer == '-':
        exit('Спасибо за игру!\nВсего наилучшего!')
get_word()