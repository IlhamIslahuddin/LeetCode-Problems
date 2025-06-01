class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [0 for i in range (len(nums))]
        for i in range (len(nums)):
            value = nums[i]
            for j in range (len(nums)):
                if nums[j] < value:
                    arr[i] += 1
        return arr
