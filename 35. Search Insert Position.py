class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range (len(nums) - 1):
            if target <= nums[i]:
                return i

            elif target > nums[i] and i == (len(nums) - 2):
                return len(nums)
