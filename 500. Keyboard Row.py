class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = ["q","w","e","r","t","y","u","i","o","p"]
        row2 = ["a","s","d","f","g","h","j","k","l"]
        row3 = ["z","x","c","v","b","n","m"]
        remove = []
        for word in words:
            if word[0].lower() in row1:
                row = 1
            elif word[0].lower() in row2:
                row = 2
            elif word[0].lower() in row3:
                row = 3
            for i in range (1,len(word)):
                char = word[i].lower()
                if (row == 1 and char not in row1) or (row == 2 and char not in row2) or (row == 3 and char not in row3):
                    remove.append(word)
                    break
        for x in remove:
            words.remove(x)
        return words
