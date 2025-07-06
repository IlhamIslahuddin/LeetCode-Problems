class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s = str(num)
        reversed_1 = s[::-1]
        if len(str(num)) == 1:
            return True
        while reversed_1[0] == "0":
            reversed_1 = reversed_1[1:]
        reversed_2 = reversed_1[::-1]
        while reversed_2[0] == "0":
            reversed_2 = reversed_2[1:]
        if int(reversed_2) == num:
            return True
        else:
            return False
