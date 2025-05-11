class Solution:
    def reverse(self, x: int) -> int:
        s = ""
        string = str(x)
        if len(string) == 1:
            return x
        minus = False
        if string[0] == "-":
            minus = True
            string = string[1::]
        for char in string:
            s = char + s
        if s[0] == "0":
            s = s[1::]
        if minus == True:
            s = "-" + s
        if int(s) < (-2)**31 or int(s) > (2 ** 31) - 1:
            return 0
        return int(s)
