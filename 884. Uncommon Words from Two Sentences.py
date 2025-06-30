class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        arr1 = s1.split(" ")
        arr2 = s2.split(" ")
        output = []
        duplicates = []
        for word in arr1:
            if word in output:
                output.remove(word)
                duplicates.append(word)
            elif word not in arr2 and word not in output:
                output.append(word)
        for word in arr2:
            if word in output:
                output.remove(word)
                duplicates.append(word)
            elif word not in arr1 and word not in output:
                output.append(word)
        for word in duplicates:
            if word in output:
                output.remove(word)
        return output
