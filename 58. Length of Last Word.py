class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        newstring = s.split(" ")
        num_spaces = 1
        while len(newstring[(num_spaces)*-1]) == 0:
            num_spaces += 1
        return len(newstring[(num_spaces)*-1])
