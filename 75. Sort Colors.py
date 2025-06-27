class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range (len(nums)):
            position = i
            val = nums[position]
            while position > 0 and val < nums[position - 1]:
                nums[position] = nums[position - 1]
                nums[position - 1] = val
                position -= 1
                val = nums[position]
