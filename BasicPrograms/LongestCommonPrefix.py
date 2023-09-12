class Solution:
    def longestCommonPrefix(self, lst: List[str]) -> str:
        ans=""
        lst=sorted(lst)
        first=lst[0]
        last=lst[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans