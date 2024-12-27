class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            digits = [int(n) for n in str(num)] ## creates array for each char in str(num)
            num = sum(digits)
        return num
