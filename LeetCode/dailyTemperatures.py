class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result: List[int] = [0]*len(temperatures)
        #so rest of the values will be zero
        stack: List[int] = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()# memory 
                result[stackIndex] = i-stackIndex
                
            stack.append([t, i])
        return result
