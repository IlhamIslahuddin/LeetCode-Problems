class Solution:
    def finalString(self, s: str) -> str:
        new_str = ""
        for char in s:
            if char == "i":
                temp = ""
                for i in range (len(new_str)):
                    temp += new_str[-i-1]
                new_str = temp
            else:
                new_str += char
        return new_str
