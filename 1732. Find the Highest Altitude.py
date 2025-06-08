class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr = [0]   
        net = 0
        for i in range(len(gain)):
            net += gain[i]
            arr.append(net)
        return max(arr)
