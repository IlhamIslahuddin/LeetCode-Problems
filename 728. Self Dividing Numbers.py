class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        counter = left
        arr = []
        while counter <= right:
            for digit in str(counter):
                self_dividing = True
                if int(digit) == 0 or counter % int(digit) != 0:
                    self_dividing = False
                    break
            if self_dividing == True:
                arr.append(counter)
            counter += 1
        return arr
