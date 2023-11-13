"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""


def plusOne(digits: list[int]) -> list[int]:
    digits_list = int("".join(map(str, digits)))
    digits_list += 1
    digits_list = str(digits_list)
    result_list = []
    for i in digits_list:
        result_list.append(int(i))

    return result_list

print(plusOne([1,2,3]))
