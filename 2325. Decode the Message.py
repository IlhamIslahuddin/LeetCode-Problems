class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        key_arr = []
        for char in key:
            if char != " " and char not in key_arr:
                key_arr.append(char)
        s = ""
        for char in message:
            if char == " ":
                s += char
            else:
                index = key_arr.index(char)
                s += alphabet[index]
        return s
