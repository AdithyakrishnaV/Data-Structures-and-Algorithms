class Solution:
    def isValid(self, s: str) -> bool:
        dicts: dict={'(':')', '{':'}', '[':']'}
        stack: List[str] = []
        for i in s:
            if i in dicts.keys():
                stack.append(i)
            if i in dicts.values():
               if not stack or dicts[stack.pop()] !=i:#key != value
                   return False
        return not stack #true if stack is empty