class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range (k):
            highest = max(gifts)
            index = gifts.index(highest)
            gifts[index] = int((gifts[index] ** 0.5))
        return int(sum(gifts))
