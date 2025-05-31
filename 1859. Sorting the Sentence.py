class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split(" ")
        new_str = ""
        for i in range (len(arr)+1):
            for word in arr:
                if int(word[-1]) == i:
                    new_str += word[:-1] + " "
    
        new_str = new_str[:-1]
        return new_str
