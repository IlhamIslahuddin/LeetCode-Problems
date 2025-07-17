class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alphabet = ['#','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        new_str = ""
        num = 0
        for char in s:
            new_str += str(alphabet.index(char))
        for i in range (k):
            for digit in new_str:
                num += int(digit)
            new_str = str(num)
            num = 0
        return int(new_str)
