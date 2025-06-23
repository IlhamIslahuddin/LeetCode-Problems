class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] = dict[num] + 1
            else:
                dict[num] = 1
        val = max(dict.values())
        for k, v in dict.items():
            if v == val:
                return k
