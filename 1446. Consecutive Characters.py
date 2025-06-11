class Solution:
    def maxPower(self, s: str) -> int:
        max = 0
        if len(s) == 1:
            return 1
        for i in range (len(s)-1):
            count = 1
            char = s[i]
            n = i + 1
            while  n < (len(s)) and char == s[n]:
                count += 1
                char = s[n]
                n += 1
            if count > max:
                max = count
        return max
