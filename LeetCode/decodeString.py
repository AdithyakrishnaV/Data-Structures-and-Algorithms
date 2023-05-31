class Solution:
    def decodeString(self, s: str) -> str:
        stack: List[int] = []

        for i in s:
            if i !=  "]":
                stack.append(i)
            else:
                string: str = ""
                while stack[-1] != "[":
                    string = stack.pop() + string

                stack.pop() #pop "["
                
                k: str = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k) * string)

        return "".join(stack)
