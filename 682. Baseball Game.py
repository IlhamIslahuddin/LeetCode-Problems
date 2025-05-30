class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for op in operations:
            if op == "+":
                num = arr[len(arr)-1] + arr[len(arr)-2]
                arr.append(num)
            elif op == "D":
                arr.append(arr[len(arr)-1]*2)
            elif op == "C":
                arr.pop(-1)
            else:
                arr.append(int(op))
        return sum(arr)
