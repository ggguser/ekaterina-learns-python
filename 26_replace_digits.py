# Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.

#Пример.
#Input                              #Output
#8 5 12 12 15                      hello
#8 5 12 12 15 , 0 23 15 18 12 4 !  hello, world!


def convert_digits_to_char_0(input_digits):
    chars = []
    for part in input_digits.split(sep=' '):
        if part.isdigit():
            chars.append(chr(int(part)))
        else:
            chars.append(part)
    return ''.join(chars)


def convert_digits_to_char_1(numbers):
    import string
    alphabet = string.ascii_uppercase
    numbers = numbers.split()
    letters = ''
    for number in numbers:
        if number.isdigit():
            letters += alphabet[int(number) - 1]
        else:
            letters += number

    print(''.join(letters))


def convert_digits_to_char_2(numbers):
    letters = ''
    for num in numbers.split():
        if num.isdigit():
            letters += f'{chr(int(num) + 96)}'
        else:
            letters += num
    return letters


if __name__ == '__main__':
    print(convert_digits_to_char_0('8 5 12 12 15 , 0 23 15 18 12 4 !'))
    print(convert_digits_to_char_1('8 5 12 12 15 , 0 23 15 18 12 4 !'))
    print(convert_digits_to_char_2('8 5 12 12 15 , 0 23 15 18 12 4 !'))

