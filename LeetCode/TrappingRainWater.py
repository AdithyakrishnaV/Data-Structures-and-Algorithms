class Solution:
    def trap(self, height: List[int]) -> int:

        l, r= 0, len(height) -1
        maxL, maxR = height[l], height[r]
        result = 0

        while l < r:
            
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                result += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                result += maxR - height[r]

        return result