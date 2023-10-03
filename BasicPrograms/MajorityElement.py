class Solution(object):
    def majorityElement(self, nums):
        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1

        count = len(nums)//2
        majority_element = 0
        for num in num_count:
            if num_count[num] > count:
                majority_element = num
        
        return majority_element
        
