class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = []
        seen_twice =[]
        for num in nums:
            if num not in seen_once:
                seen_once.append(num)
            else:
                seen_twice.append(num)
        for num in nums:
            if num not in seen_twice:
                return num
