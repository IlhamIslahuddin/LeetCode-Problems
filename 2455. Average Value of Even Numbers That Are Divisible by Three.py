class Solution:
    def averageValue(self, nums: List[int]) -> int:
        div = 0
        total = 0
        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                div += 1
                total += num
        try:
            return total // div
        except ZeroDivisionError:
            return 0
