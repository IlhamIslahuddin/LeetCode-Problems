class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        total = 0
        s = str(x)
        for digit in s:
            total += int(digit)
        if x % total == 0:
            return total
        else:
            return -1
