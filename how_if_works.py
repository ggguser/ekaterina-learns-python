if __name__ == '__main__':
    a = 'АБВ'
    letter = 'a'
    if letter in a:
        print("if 'A' in a:")
    elif letter.lower() in a.lower():
        print("elif letter.lower() in a.lower():")
    else:
        print('else')