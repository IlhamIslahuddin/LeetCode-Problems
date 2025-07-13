class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        nums.insert(0,0)
        n = len(nums) - 1
        special = []
        total = 0
        for i in range (1,n+1):
            if n % i == 0:
                special.append(nums[i])
        for num in special:
            total += (num**2)
        return total
