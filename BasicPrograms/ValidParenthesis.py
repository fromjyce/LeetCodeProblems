class Solution:
    def isValid(self, s: str) -> bool:
        opening_chars = ["(", "{", "["]
        closing_chars = [")", "}", "]"]
        s = list(s)
        result = []
        for exp in s:
            if exp in opening_chars:
                result.append(exp)
            elif exp in closing_chars:
                if len(result) == 0:
                    return False 
                top_char = result.pop()
                if opening_chars.index(top_char) != closing_chars.index(exp):
                    return False
        return len(result)==0