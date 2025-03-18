# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        mid = (low + high) // 2
        found = False
        while found == False:
            if isBadVersion(mid) == True:
                high = mid - 1
                if isBadVersion(mid-1) == False:
                    found = True
                    return mid
            else:
                low = mid + 1
            mid = (low + high) // 2
