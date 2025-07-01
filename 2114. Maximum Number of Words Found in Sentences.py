class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max = 0
        for sentence in sentences:
            arr = sentence.split(" ")
            count = len(arr)
            if count > max:
                max = count
        return max
