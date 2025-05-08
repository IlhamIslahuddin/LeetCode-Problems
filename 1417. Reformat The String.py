class Solution:
    def reformat(self, s: str) -> str:
        if len(s) == 1:
            return s
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        digits = ["0","1","2","3","4","5","6","7","8","9"]
        alph_count = 0
        alph_arr = []
        digit_count = 0
        digit_arr = []
        new_str = ""
        for char in s:
            if char in alphabet:
                alph_count += 1
                alph_arr.append(char)
            elif char in digits:
                digit_count += 1
                digit_arr.append(char)
        if (alph_count == 0 or digit_count == 0) or abs(alph_count - digit_count) >= 2:
            return ""
        else:
            if len(alph_arr) > len(digit_arr):
                n = len(digit_arr)
                alph_longer = True
            elif len(alph_arr) < len(digit_arr):
                n = len(alph_arr)
                alph_longer = False
            else:
                n = len(alph_arr)
                alph_longer = None
            for i in range (n):
                if alph_longer == True or alph_longer == None:
                    new_str = new_str + alph_arr[i]
                    new_str = new_str + digit_arr[i]
                elif alph_longer == False:
                    new_str = new_str + digit_arr[i]
                    new_str = new_str + alph_arr[i]
            if alph_longer == True:
                new_str = new_str + alph_arr[n]
            elif alph_longer == False:
                new_str = new_str + digit_arr[n]
            return new_str
