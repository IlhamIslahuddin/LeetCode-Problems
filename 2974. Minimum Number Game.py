class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        while len(nums) > 0:
            n = min(nums)
            i = nums.index(n)
            val1 = nums.pop(i)
            x = min(nums)
            y = nums.index(x)
            val2 = nums.pop(y)
            arr.append(val2)
            arr.append(val1)
        return arr
