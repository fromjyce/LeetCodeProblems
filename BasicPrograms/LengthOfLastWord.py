class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.strip(" ").split(" ")
        length = len(lst)
        return len(lst[length-1])