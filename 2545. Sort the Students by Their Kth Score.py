class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        for i in range (len(score)):
            position = i
            value = score[position][k]
            while position > 0 and value > score[position-1][k]:
                temp = score[position]
                score[position] = score[position-1]
                score[position-1] = temp
                position -= 1
                value = score[position][k]
        return score
