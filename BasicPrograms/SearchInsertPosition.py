"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""


def searchInsert(nums, target) -> int:
    if target in nums:
        return nums.index(target)
    nums.append(target)
    nums = sorted(nums)
    return nums.index(target)


print(searchInsert([1, 3, 5, 6], 2))


# Another Way of doing this


def searchInsert(nums, target) -> int:
    left, right = 0, len(nums) - 1
        
    while left <= right:
        mid = left + (right - left) // 2
            
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

