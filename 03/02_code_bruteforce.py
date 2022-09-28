# Известно, что сейф открывается при правильном вводе
# кода из 3 цифр 0...9. Задайте код и затем откройте сейф,
# используя метод перебора с помощью нескольких операторов цикла for

import random


def generate_code():
    return [random.randint(0, 9) for _ in range(3)]


def bruteforce_code(code):
    for first_digit in range(0, 10):
        for second_digit in range(0, 10):
            for third_digit in range(0, 10):
                guess = [first_digit, second_digit, third_digit]
                if guess == code:
                    return guess


if __name__ == '__main__':
    code = generate_code()
    print(code)

    print(bruteforce_code(code))
