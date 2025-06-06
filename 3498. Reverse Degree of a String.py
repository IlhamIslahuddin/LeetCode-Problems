class Solution:
    def reverseDegree(self, s: str) -> int:
        reversed_alphabet = ["",'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
        sum = 0
        s = "x" + s #adds buffer to the front to make the string 1-indexed
        for i in range(1,len(s)):
            index1 = i
            index2 = reversed_alphabet.index(s[i])
            sum += index1 * index2
        return sum
