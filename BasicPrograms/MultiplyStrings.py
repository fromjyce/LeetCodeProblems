"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


def multiply(num1: str, num2: str) -> str:
    dic = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "0": 0,
    }
    num1_list = []
    num2_list = []
    for j in num1:
        if j in dic.keys():
            num1_list.append(dic[j])
    for j in num2:
        if j in dic.keys():
            num2_list.append(dic[j])

    num1_int = int("".join(map(str, num1_list)))
    num2_int = int("".join(map(str, num2_list)))

    return str(num1_int * num2_int)





print(multiply("3", "2"))
