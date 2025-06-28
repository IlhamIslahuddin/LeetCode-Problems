class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        arr = [char for char in word]
        try:
            index = arr.index(ch)
        except:
            return word
        for i in range ((index+1) // 2):
            arr[i], arr[index-i] = arr[index-i], arr[i]
        return "".join(arr)
