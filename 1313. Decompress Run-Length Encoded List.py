class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        main_arr = []
        for i in range(0,len(nums),2):
            temp = [nums[i+1] for j in range(nums[i])]
            for num in temp:
                main_arr.append(num)
        return main_arr
