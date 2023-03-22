class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i]+nums[j] == target):
                    print([",".join([str(i), str(j)])])
                    #return(i,j)  --> do this when running on leetcode because :
                    #The print() function simply outputs the result to the console, but it doesn't actually return the result to the calling function or test case.
                    break


nums = [2, 7, 11, 15]
target = 9

solution = Solution()
solution.twoSum(nums, target)
