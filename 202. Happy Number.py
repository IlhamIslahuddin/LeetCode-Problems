class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        happy = False
        looping = False
        while happy == False and looping == False:
            seen.append(n)
            newn = 0
            for i in range(len(str(n))):
                newn += int(str(n)[i])**2
            n = newn
            if n == 1:
                happy = True
            elif n in seen:
                looping = True
        return happy
