# todo: Шифр Цезаря
# Описание шифра.
# В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
# является одним из самых простых и широко известных методов шифрования.
# Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
# фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
# E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

# Задача.
# Считайте файл message.txt и зашифруйте текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.


CYRILLIC_UPPERCASE = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
CYRILLIC_LOWERCASE = CYRILLIC_UPPERCASE.lower()
CYRILLIC_LETTERS = CYRILLIC_UPPERCASE + CYRILLIC_LOWERCASE


def encode_ceasar(input_string, shift):
    shift = shift + 1
    encoded_string = ''
    for char in input_string:
        if char in CYRILLIC_UPPERCASE:
            char_index = CYRILLIC_UPPERCASE.index(char)
            encoded_string += CYRILLIC_UPPERCASE[char_index-shift]
        elif char in CYRILLIC_LOWERCASE:
            char_index = CYRILLIC_LOWERCASE.index(char)
            encoded_string += CYRILLIC_LOWERCASE[char_index-shift]
        else:
            encoded_string += char
    return encoded_string


if __name__ == '__main__':
    encoded_lines = []
    with open('message.txt') as f:
        lines = f.readlines()
        for index, line in enumerate(lines, start=1):
            encoded_lines.append(encode_ceasar(line, index))

    with open('encoded_message.txt', 'w') as f:
        f.writelines(encoded_lines)

