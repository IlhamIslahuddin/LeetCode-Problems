class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        changed = False
        output = ""
        for char in s:
            if char == "6" and changed == False:
                output += "9"
                changed = True
            else:
                output += char
        return int(output)
