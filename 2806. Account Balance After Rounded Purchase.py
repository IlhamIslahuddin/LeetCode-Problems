class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        n = purchaseAmount % 10
        if n >= 5:
            return 100 - (purchaseAmount + (10-n))
        else:
            return 100 - (purchaseAmount - n)
