class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = ""
        s2 = ""
        for word in word1:
            s1 = s1 + word
        for word in word2:
            s2 = s2 + word
        if s1 == s2:
            return True
        else:
            return False
