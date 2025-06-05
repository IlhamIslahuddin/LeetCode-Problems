class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output_arr = []
        for kid in candies:
            if kid + extraCandies >= max(candies):
                output_arr.append(True)
            else:
                output_arr.append(False)
        return output_arr
