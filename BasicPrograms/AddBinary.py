class Solution:
    def addBinary(self, no1: str, no2: str) -> str:
        max_len = max(len(no1), len(no2))
        no1 = no1.zfill(max_len)
        no2 = no2.zfill(max_len)
        result = ''
        carry = 0
        for i in range(max_len - 1, -1, -1):
            r = carry
            r += 1 if no1[i] == '1' else 0
            r += 1 if no2[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result
            carry = 0 if r < 2 else 1
        if carry != 0:
            result = '1' + result
        return result.zfill(max_len)