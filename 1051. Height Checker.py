class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = len(heights)
        total = 0
        expected = [height for height in heights]
        expected.sort()
        for i in range(n):
            if heights[i] != expected[i]:
                total += 1
        return total
