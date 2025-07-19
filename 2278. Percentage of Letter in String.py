class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = 0
        for char in s:
            if char == letter:
                n += 1
        return int((n / len(s) * 100))
