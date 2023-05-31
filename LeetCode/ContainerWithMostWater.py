class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA: int=0
        l: int=0
        r: int=len(height)-1

        while l < r:
            h: int=min(height[l], height[r])
            maxA = max(maxA, (h * (r-l)))

            if h==height[l]:
                l =l+1
            else:
                r =r-1
        return maxA   