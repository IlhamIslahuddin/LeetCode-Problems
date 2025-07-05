class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        done = False
        x = original
        while done == False:
            for i in range (len(nums)):
                done = True
                if nums[i] == x:
                    x = x * 2
                    done = False
                    break
        return x
