class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        for i in range (len(nums) // 2):
            minElement = min(nums)
            maxElement = max(nums)
            nums.pop(nums.index(minElement))
            nums.pop(nums.index(maxElement))
            average = (minElement + maxElement) / 2
            averages.append(average)
        return min(averages)
