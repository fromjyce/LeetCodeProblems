"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""


def missingNumber(nums: list[int]) -> int:
    n = len(nums)
    value = 0
    for i in range(0, n + 1):
        if i not in nums:
            value = i

    return value


print(missingNumber([0, 1, 3]))


# Another Method


def missingNumber2(nums: list[int]) -> int:
    n = len(nums)
    return ((n * (n + 1)) // 2) - (sum(nums))


print(missingNumber2([0, 1, 3]))
