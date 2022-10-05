import random


# Поле чудес, программа рандомно выбирает вопрос из списка,
# ответ в др списке с одним ключом.
# Пользователь вводит буквы. 10 попыток


answers = ["оператор", "функция", "класс"]
questions = [
    "Наименьшая автономная часть языка программирования",
    "Выделенный блок кода, выполняющий определенную операцию",
    "модель для создания объектов определённого типа, описывающая их структуру "
]

index = random.randrange(0, len(answers))

question = questions[index]
answer = answers[index].upper()

print('Вопрос:', question)
print(f'{len(answer)} букв')
print('▮' * len(answer))

max_penalty_points = 10
penalty_points = 0
guessed_letters = []
while penalty_points < max_penalty_points:
    print('Введите букву: ')
    try_letter = str(input()).upper()

    if try_letter in answer:
        print('Есть такая буква!')
        guessed_letters.append(try_letter)
        masked_word = answer
        for letter in answer:
            if letter not in guessed_letters:
                masked_word = masked_word.replace(letter, '▮')
        print(masked_word)
        if masked_word == answer:
            print('Угадано! У вас штрафных баллов: ', penalty_points)
            break

    else:
        penalty_points += 1
        print('нет такой буквы, штрафных баллов: ', penalty_points)
        if penalty_points == max_penalty_points:
            print('Вы проиграли!')
