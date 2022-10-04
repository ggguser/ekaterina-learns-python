# Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.
#
#
# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.
import string


def decode_ceasar(encoded_string, shift):
    shift += 1
    decoded_string = ''
    for char in encoded_string:
        if char in string.ascii_lowercase:
            char_index = string.ascii_lowercase.index(char)
            decoded_string += string.ascii_lowercase[char_index-shift]
        else:
            decoded_string += char
    return decoded_string


if __name__ == '__main__':
    for shift in range(len(string.ascii_lowercase)):
        print(decode_ceasar("grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.", shift))
