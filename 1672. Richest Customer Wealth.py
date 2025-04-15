class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        highest = 0
        for account in accounts:
            if sum(account) > highest:
                highest = sum(account)
        return highest
