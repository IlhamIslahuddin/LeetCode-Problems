class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = 0
        digit_sum = 0
        for num in nums:
            element_sum += num
            if num >= 10:
                string = str(num)
                arr = [int(string[i]) for i in range(len(string))]
                for n in arr:
                    digit_sum += n
            else:
                digit_sum += num
        return abs(element_sum - digit_sum)
