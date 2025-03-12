class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        array = []
        for i in range(n):
            array.append(1)
        add = [array]
        array = add
        for i in range(m):
            array = array + add
        
        for i in range(1, m):
            for j in range(1, n):
                array[i][j] = array[i-1][j] + array[i][j-1]
        
        return array[m-1][n-1]
