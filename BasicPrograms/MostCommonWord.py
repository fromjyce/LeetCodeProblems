import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        pattern = r'[^a-zA-Z0-9\s]'
        cleaned_paragraph = re.sub(pattern, ' ', paragraph.lower())
        words = cleaned_paragraph.replace(".","").split()
        word_count = {}
        for word in words:
            if word not in banned:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        most_freq_word = None
        most_freq_count = 0
        for word, count in word_count.items():
            if count > most_freq_count:
                most_freq_word = word
                most_freq_count = count

        return most_freq_word
