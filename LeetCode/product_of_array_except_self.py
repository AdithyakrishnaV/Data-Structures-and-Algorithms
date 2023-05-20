class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result: List[int]=[1] * len(nums)
        #without division
        
        pre=1
        for i in range(len(nums)):
            result[i]=pre #[1,1,2,6]
            pre= pre * nums[i]
        
        post=1
        for i in range(len(nums) -1,-1,-1):
            result[i]= result[i]*post #[24,12,8,6]
            post= post * nums[i]
        return result