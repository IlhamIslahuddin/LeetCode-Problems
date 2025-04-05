class Solution:
    def arrangeCoins(self, n: int) -> int:
        x = n
        for i in range(1,n+1):
            if x - i > 0:
                x -= i
            elif x - i == 0:
                return i
            else:
                return i-1
