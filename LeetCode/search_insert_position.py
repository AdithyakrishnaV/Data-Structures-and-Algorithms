
#Time complexity O(log n)
class Solution:
    def searchInsert(self,nums: List[int], target: int) -> int:
        if not nums:
            return 0
        else:
            n: int=len(nums)
            l: int=0
            r: int=n-1
            while(l<r):
                mid=l+(r-l)//2 #1+(3-1)/2 = 2-index
                if nums[mid]==target: return mid
                elif target < nums[mid]:
                    r=mid
                else:
                    l=mid+1
            return l+1 if target > nums[l] else l


# Time complexity O(n)

class Solution:
    def searchInsert(self,nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            i=0
            for i in range(len(nums)):
                if target < nums[i]:
                    return i
            return i+1   