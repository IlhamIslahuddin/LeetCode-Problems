class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = []
        n = len(grid)
        repeated = 0
        all_numbers = [i for i in range(1,n**2+1)]
        for i in range (n):
            for j in range(n):
                if grid[i][j] not in seen:
                    seen.append(grid[i][j])
                else:
                    repeated = grid[i][j]
        for num in all_numbers:
            if num not in seen:
                return [repeated,num] 
