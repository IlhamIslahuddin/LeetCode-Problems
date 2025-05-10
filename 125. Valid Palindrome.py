class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        digits = ["0","1","2","3","4","5","6","7","8","9"]
        for char in s:
            char = char.lower()
            if char in alphabet or char in digits:
                new_s = new_s + char
        n = len(new_s)
        for i in range (n // 2):
            if new_s[i] != new_s[n-i-1]:
                return False
        return True
