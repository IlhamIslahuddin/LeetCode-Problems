class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = list(s)
        if len(s) != len(t):
            return False
        for char in t:
            if char in arr:
                arr.remove(char)
            else:
                return False
        return True
