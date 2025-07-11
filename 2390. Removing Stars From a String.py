class Solution:
    def removeStars(self, s: str) -> str:
        arr = []
        for char in s:
            if char != "*":
                arr.append(char)
            else:
                arr.pop(-1)
        return "".join(arr)
