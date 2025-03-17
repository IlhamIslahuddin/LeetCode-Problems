class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = []
        for i in range(1,rowIndex+2): #instead of n+1 since it needs to return arr[n]
            array = [1 for _ in range(i)]
            if i > 2:
                x = 1
                while x < i-1:
                    array[x] = arr[i-2][x] + arr[i-2][x-1]
                    x += 1
            arr.append(array)
        return arr[rowIndex]
