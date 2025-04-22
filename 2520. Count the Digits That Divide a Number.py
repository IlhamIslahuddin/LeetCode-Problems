class Solution:
    def countDigits(self, num: int) -> int:
        s = str(num)
        count = 0
        for char in s:
            if num % int(char) == 0:
                count += 1
        return count
