class Solution:
    def countEven(self, num: int) -> int:
        arr = []
        for i in range (1,num+1):
            x = 0
            for char in str(i):
                x += int(char)
            if x % 2 == 0:
                arr.append(i)
        return len(arr)
