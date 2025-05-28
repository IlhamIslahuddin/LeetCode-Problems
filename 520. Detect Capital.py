class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        word_type = 0
        if len(word) == 1:
            return True
        elif len(word) == 2:
            word_type = 4
        else:
            if word[0] in capitals and word[1] in capitals:
                word_type = 1
            elif word[0] in capitals and word[1] not in capitals:
                word_type = 2
            elif word[0] not in capitals and word[1] not in capitals:
                word_type = 3
            else:
                return False
        if word_type == 1:
            for i in range (2,len(word)):
                if word[i] not in capitals:
                    return False
            return True
        elif word_type == 4:
            if word[0] in capitals and word[1] not in capitals:
                return True
            if word[0] not in capitals and word[1] not in capitals:
                return True
            if word[0] in capitals and word[1] in capitals:
                return True
            else:
                return False  
        else:
            for i in range (2,len(word)):
                if word[i] in capitals:
                    return False
            return True
