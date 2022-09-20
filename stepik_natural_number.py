def get_number():
    number = int(input('Введите натуральное число\n'))
    if not number > 0:
        print('Натуральное число должно быть > 0')
        return None
    return number


def manipulate_natural_number(number):
    number_as_digits = [int(char) for char in str(number)]

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
    if input_number is not None:
        manipulate_natural_number(input_number)
