"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""


def singleNumber(nums: list[int]) -> int:
    dictn = {}
    for num in nums:
        if num in dictn:
            dictn[num] += 1
        else:
            dictn[num] = 1
    value = list({i for i in dictn if dictn[i] == 1})
    result = int("".join(map(str, value)))
    return result


print(singleNumber([4, 4, 2]))

# Another Method


def singleNumber(nums: list[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result

print(singleNumber([4, 4, 2]))