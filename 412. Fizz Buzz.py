class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range (1,n+1):
            answer.append(str(i))
            if i % 5 == 0 and i % 3 == 0:
                answer[i-1] = "FizzBuzz"
            elif i % 5 == 0:
                answer[i-1] = "Buzz"
            elif i % 3 == 0:
                answer[i-1] = "Fizz"
        return answer
