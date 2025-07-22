class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        total = 0
        for i in range (k):
            if numOnes > 0:
                total += 1
                numOnes -= 1
            elif numOnes <= 0 and numZeros > 0:
                numZeros -= 1
            else:
                total -= 1
                numNegOnes -= 1
        return total
