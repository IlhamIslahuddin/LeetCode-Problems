class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for passenger in details:
            s = "" + passenger[-4] + passenger[-3]
            if int(s) > 60:
                count += 1
        return count 
