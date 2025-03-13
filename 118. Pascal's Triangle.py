class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []
        for i in range(1,numRows+1):
            array = [1 for _ in range(i)]
            if i > 2:
                x = 1
                while x < i-1:
                    array[x] = arr[i-2][x] + arr[i-2][x-1]
                    x += 1
            arr.append(array)
        return arr
