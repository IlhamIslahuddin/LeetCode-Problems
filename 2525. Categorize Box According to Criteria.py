class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        heavy = False
        bulky = False
        if length >= (10**4) or width >= (10**4) or height >= (10**4) or (length * width * height) >= (10**9):
            bulky = True
        if mass >= 100:
            heavy = True
        if heavy == True and bulky == True:
            return "Both"
        elif heavy == True and bulky == False:
            return "Heavy"
        elif heavy == False and bulky == True:
            return "Bulky"
        else:
            return "Neither"
