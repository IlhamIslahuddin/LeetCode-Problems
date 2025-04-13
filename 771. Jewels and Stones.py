class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_array = [jewels[i] for i in range(len(jewels))]
        count = 0
        for i in range(len(stones)):
            if stones[i] in jewel_array:
                count += 1
        return count
