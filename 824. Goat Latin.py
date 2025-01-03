class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ['a','e','i','o','u']
        s = sentence.split(" ")
        new = []
        counter = 1
        for word in s:
            if counter > 1:
                if (word[0].lower()) in vowels:
                    new.append(" " + word + "ma" + "a"*(counter))
                else:
                    word = word[1::] + word[0]
                    new.append(" " + word + "ma" + "a"*(counter))
            else:
                if (word[0].lower()) in vowels:
                    new.append(word + "ma" + "a"*(counter))
                else:
                    word = word[1::] + word[0]
                    new.append(word + "ma" + "a"*(counter))
            counter += 1
        new_s = ''.join(new)
        return new_s
