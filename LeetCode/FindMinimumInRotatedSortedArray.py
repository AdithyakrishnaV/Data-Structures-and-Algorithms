class Solution:
    def findMin(self, nums: List[int]) -> int:
        result: int=nums[0]
        l, r = 0, len(nums)-1

        while l < r:
            mid = (l+r)//2
            result = min(result, nums[mid])
            if nums[r] < nums[mid]:
                l = mid +1
            else:
                r = mid - 1
        
        return min(result, nums[l])   