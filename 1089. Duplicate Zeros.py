class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count = 0
        n = len(arr)
        temp = n
        while count < n:
            if arr[count] == 0:
                arr.insert(count+1,0)
                count += 2
                n += 1
            else:
                count += 1
        del arr[temp:]
