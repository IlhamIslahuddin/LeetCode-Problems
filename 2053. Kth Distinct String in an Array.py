class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct = [x for x in arr if arr.count(x) == 1]
        try:
            return distinct[k-1]
        except:
            return ""
