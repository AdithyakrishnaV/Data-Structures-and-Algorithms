class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack: List[str]=[]
        result: List[str]=[]

        def trackN(open: int,close: int):

            if open == close == n:
                result.append("".join(stack))
                return
                
            
            if open < n:
                stack.append("(")
                trackN(open +1, close)
                stack.pop()

            if close < open:
                stack.append(")")
                trackN(open, close +1)
                stack.pop()
        trackN(0,0)
        return result