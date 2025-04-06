class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        time = arrivalTime + delayedTime
        if time == 24:
            return 0
        elif time > 24:
            return time - 24
        else:
            return time
