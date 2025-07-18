class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        arr = []
        n = nums.count(target)
        nums.sort()
        for i in range (n):
            if nums.index(target) in arr:
                arr.append (arr[i-1] + 1)
            else:
                arr.append(nums.index(target))
            
        return arr
