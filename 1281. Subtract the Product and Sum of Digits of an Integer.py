class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        product = 1
        sum = 0
        for char in s:
            product = product * int(char)
            sum += int(char)
        return product - sum
