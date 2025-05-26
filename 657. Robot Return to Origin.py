class Solution:
    def judgeCircle(self, moves: str) -> bool:
        verticals = 0
        horizontals = 0
        for move in moves:
            if move == "L":
                horizontals -= 1
            elif move == "R":
                horizontals += 1
            elif move == "U":
                verticals += 1
            elif move == "D":
                verticals -= 1
        if verticals != 0 or horizontals != 0:
            return False
        return True
