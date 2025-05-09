class Solution:
    def checkString(self, s: str) -> bool:
        if s[0] == "a":
            is_a = True
        else:
            is_a = False
        for char in s:
            if is_a == False and char == "a":
                return False
            elif char == "b":
                is_a = False
        return True
