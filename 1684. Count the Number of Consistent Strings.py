class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_arr = [char for char in allowed]
        count = 0
        is_allowed = True
        for word in words:
            is_allowed = True
            for char in word:
                if char not in allowed_arr:
                    is_allowed = False
                    break
            if is_allowed == True:
                count += 1
            
        return count
