class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        if len(word1) > len(word2):
            word1_longer = True
            n = len(word2)
        elif len(word1) < len(word2):
            word1_longer = False
            n = len(word1)
        else:
            n = len(word1)
            word1_longer = False
        for i in range(n):
            merged = merged + word1[i]
            merged = merged + word2[i]
        if len(word1) == len(word2):
            return merged
        elif word1_longer == True:
            merged = merged + word1[n:]
            return merged
        elif word1_longer == False:
            merged = merged + word2[n:]
            return merged
