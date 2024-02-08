# предыдущие функции добавлены скрыто для тестов

import random


def add_numbers(a, b):
    dey = ['+', '-', '*', '/']
    try:
        sum1 = random.randint(a, b)
        sum2 = random.randint(a, b)
        operator = random.choice(dey)
        return f'{sum1} {operator} {sum2}'
    except:
        print('Ввод неправильный! Можно вводить только числа!')


def check_answer(primer, answer):
    try:
        a = eval(primer)
        if a == float(answer):
            return True
        else:
            return False
    except ValueError:
        return False


def math_quiz(number_of_questions=5):
    print("Добро пожаловать в математический тест!")
    correct_answers = 0

    for i in range(number_of_questions):
        primer = add_numbers(1, 5)
        user_answer = input(f"{primer}: ")
        b = check_answer(primer, user_answer)
        if b == True:
            correct_answers += 1

    print("Тест завершен.")
    print(f"Вы правильно решили {correct_answers} из {number_of_questions} вопросов.")

    if number_of_questions * 0.8 <= correct_answers:
        print("Отлично! Вы получаете оценку A.")
    elif number_of_questions * 0.6 <= correct_answers and number_of_questions * 0.8 > correct_answers:
        print("Хорошо! Вы получаете оценку B.")
    else:
        print("Попробуйте еще раз. Вы получаете оценку C.")


math_quiz(7)