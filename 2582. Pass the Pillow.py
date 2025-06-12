class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        position = 1
        going_right = True
        for i in range (time):
            if going_right == True:
                position += 1
            else:
                position -= 1
            if position == n:
                going_right = False
            if position == 1:
                going_right = True
        return position
