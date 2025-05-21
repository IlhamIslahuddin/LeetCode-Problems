class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = [letter for letter in magazine]
        for char in ransomNote:
            if char not in letters:
                return False
            else:
                letters.remove(char)
        return True
