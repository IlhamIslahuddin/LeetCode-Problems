class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target > nums[0]:
                return 1
            else:
                return 0
        for i in range (len(nums)):
            if target <= nums[i]:
                return i

            elif target > nums[i] and i == (len(nums) - 1):
                return len(nums)
