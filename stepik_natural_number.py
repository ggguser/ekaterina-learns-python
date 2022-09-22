from typing import List


def get_number():
    return input('Введите натуральное число\n')


def is_number_natural(number) -> bool:
    try:
        number = int(number)
    except ValueError:
        print('Это не натуральное число')
        return False

    if not number > 0:
        print('Натуральное число должно быть > 0')
        return False
    return True


def convert_int_to_list(number: int, base=10) -> List[int]:
    """
    >>>convert_int_to_list(123)
    [1, 2, 3]
    """
    remainder = number
    digits_list = []
    while remainder != 0:
        last_digit = remainder % base
        digits_list.append(last_digit)

        remainder //= base
    return digits_list[::-1]


def manipulate_natural_number(number):
    # number_as_digits = [int(char) for char in str(number)]
    number_as_digits = convert_int_to_list(number)

    sum_digits = 0
    for digit in number_as_digits:
        sum_digits += digit

    number_length = len(number_as_digits)

    number_factorial = 1
    for digit in number_as_digits:
        number_factorial *= digit

    number_average = sum(number_as_digits)/number_length
    first_digit = number_as_digits[0]
    sum_first_and_last_digits = number_as_digits[0] + number_as_digits[-1]

    print(f'{sum_digits=}')
    print(f'{number_length=}')
    print(f'{number_factorial=}')
    print(f'{number_average=}')
    print(f'{first_digit=}')
    print(f'{sum_first_and_last_digits=}')


if __name__ == '__main__':
    input_number = get_number()
    if is_number_natural(input_number):
        manipulate_natural_number(input_number)
