class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        arr = s.split(" ")
        new_str = ""
        for i in range(k-1):
            new_str += arr[i] + " "
        new_str += arr[k-1]
        return new_str
