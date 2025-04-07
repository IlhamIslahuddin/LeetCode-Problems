class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        distinct = self.check_distinct(nums)
        if distinct == True:
            return 0
        count = 0
        while distinct == False:
            if len(nums) > 3:
                nums = nums[-(len(nums)-3):]
            else:
                nums = []
            count += 1
            distinct = self.check_distinct(nums)
        return count

    def check_distinct(self,arr):
        seen = []
        for num in arr:
            if num in seen:
                return False
            else:
                seen.append(num)
        return True
