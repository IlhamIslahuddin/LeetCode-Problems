class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_list = list(dict.fromkeys(nums))
        if len(nums_list) < 3:
            return max(nums_list)
        else:
            nums_list.remove(max(nums_list))
            nums_list.remove(max(nums_list))
            return max(nums_list)
