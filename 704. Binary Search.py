class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bottom = 0
        top = len(nums) - 1
        while bottom <= top:
            mid = (bottom + top) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                bottom = mid + 1
            elif target < nums[mid]:
                top = mid - 1
        return -1
