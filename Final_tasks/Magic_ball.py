from random import *
answers = ['Бесспорно','Мне кажется - да','Пока неясно, попробуй снова','Даже не думай','Предрешено','Вероятнее всего','Спроси позже',
           'Мой ответ - нет','Никаких сомнений','Хорошие перспективы','Лучше не рассказывать','По моим данным - нет','Определённо да',
           'Знаки говорят - да','Сейчас нельзя предсказать','Перспективы не очень хорошие','Можешь быть уверен в этом','Да','Сконцентрируйся и спроси опять',
           'Весьма сомнительно']
def greetings():
    print('Привет, я магический шар, и я знаю ответ на любой твой вопрос.')
    print('Как я могу тебя звать?')
    name = input()
    print(f'Рад знакомству {name} \nТак какой у тебя вопрос?')
def choise():
    answer = randint(0,len(answers)-1)
    return answers[answer]
def main():
    s = input()
    print(choise())
    again()
def again():
    print('У тебя еще остались вопросы? Прошу ответь Да или Нет')
    answer = input()
    check_answer(answer)
    if answer.lower() == 'да':
        print('Так какой у тебя вопрос?')
        main()
    elif answer.lower() == 'нет':
        exit(f'Как скажешь, Возвращайся если возникнут вопросы!')
def check_answer(ans):
    while ans.lower() != 'да' and ans.lower() != 'нет':
        print('Не понимаю твой ответ, прошу ответь Да или Нет')
        ans = input()
    return ans
greetings()
main()