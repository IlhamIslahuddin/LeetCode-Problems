class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        contains = []
        for i in range(len(words)):
            for j in range (len(words[i])):
                if (words[i])[j] == x:
                    contains.append(i)
                    break
        return contains
