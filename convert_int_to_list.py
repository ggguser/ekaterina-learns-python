from typing import List


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