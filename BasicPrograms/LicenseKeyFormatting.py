class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-","").upper()
        first_seq = len(s) % k
        output_str = []
        if first_seq>0:
            output_str.append(s[:first_seq])
        
        for r in range(first_seq, len(s), k):
            output_str.append(s[r:r+k])

        return "-".join(output_str)
