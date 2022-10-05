# Убрать повторяющиеся буквы и лишние символы
# Построить по ключевой фразе часть алфавита.
# Взять все буквы по одному разу. Не буквы убрать.
# Буквы должны идти в том порядке,
# в котором встретились во фразе в первый раз.

# Input             	            Output
# apple	                            aple
# 25.04.2022 Good morning!!	       godmrni


def only_one_letter(input_string):
    output_string = ''
    for char in input_string:
        if char.isalpha() and char not in output_string:
            output_string += char.lower()

    return output_string


if __name__ == '__main__':
    print(only_one_letter('25.04.2022 Good morning !!'))

