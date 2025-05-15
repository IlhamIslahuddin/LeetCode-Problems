class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = []
        seen_twice_or_more = []
        for num in nums:
            if num not in seen:
                seen.append(num)
            else:
                seen_twice_or_more.append(num)
        for num in seen:
            if num not in seen_twice_or_more:
                return num
