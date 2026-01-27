class Solution:
    def minElement(self, nums: List[int]) -> int:
        arr = []
        for num in nums:
            arr.append(sum_of_digits(num))

        return min(arr)
def sum_of_digits(n):
    if n < 10:
        return n

    return  n % 10 + sum_of_digits(n // 10)
