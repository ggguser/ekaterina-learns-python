# Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.

#Пример.
#Input                              #Output
#8 5 12 12 15                      hello
#8 5 12 12 15 , 0 23 15 18 12 4 !  hello, world!


def convert_digits_to_char(numbers):
    letters = ''
    for num in numbers.split():
        if num.isdigit():
            letters += f'{chr(int(num) + 96)}'
        else:
            letters += num
    return letters


if __name__ == '__main__':
    print(convert_digits_to_char('8 5 12 12 15 , 0 23 15 18 12 4 !'))
