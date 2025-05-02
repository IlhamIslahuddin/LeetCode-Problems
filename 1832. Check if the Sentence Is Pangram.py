class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        if len(sentence) < 26:
            return False
        else:
            for char in sentence:
                if char in alphabet:
                    alphabet.remove(char)
            if len(alphabet) > 0:
                return False
            else:
                return True
