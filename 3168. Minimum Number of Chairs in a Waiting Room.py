class Solution:
    def minimumChairs(self, s: str) -> int:
        max = 0
        count = 0
        for second in s:
            if second == "E":
                count += 1
            else:
                count -= 1
            if count > max:
                max = count
        return max
