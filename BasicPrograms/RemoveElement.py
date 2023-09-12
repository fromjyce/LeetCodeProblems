class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        valid_elements = 0
        while i < len(nums):
            if nums[i] != val:
                nums[valid_elements] = nums[i]
                valid_elements += 1
            i += 1
        return valid_elements