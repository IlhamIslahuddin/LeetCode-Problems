class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def generate_string(curr,open_count,close_count):
            if len(curr) == n * 2:
                output.append(curr)
                return
            if open_count < n:
                generate_string(curr + "(",open_count + 1,close_count)
            #both ifs get explored
            if close_count < open_count:
                generate_string(curr + ")",open_count,close_count +1)
            
        generate_string("(",1,0)
        return output
