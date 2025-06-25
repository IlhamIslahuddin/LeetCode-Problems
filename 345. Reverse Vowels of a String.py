class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["A","a","E","e","I","i","O","o","U","u"]
        temp = ""
        arr = []
        for char in s:
            if char in vowels:
                temp += "/"
                arr.append(char)
            else:
                temp += char
        new_str = ""
        count = 0
        for char in temp:
            if char == "/":
                new_str += arr[-1-count]
                count += 1
            else:
                new_str += char
        return new_str
