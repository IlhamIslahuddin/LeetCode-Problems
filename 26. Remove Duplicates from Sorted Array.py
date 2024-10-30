class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = len(nums) - 1
        seen = []
        k = 0
        count = 0
        while count <= x:
            if nums[count] in seen:
                nums.remove(nums[count])
                x -= 1
            else:
                seen.append(nums[count])
                count += 1
        k = len(nums)
        return (k)
            
