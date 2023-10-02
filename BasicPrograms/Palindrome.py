class Solution(object):
    def isPalindrome(self, x):
        n = str(x)
        rev = n[::-1]
        if rev==n:
            return true
        else:
            return false
