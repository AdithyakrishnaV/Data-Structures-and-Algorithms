class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set: set[int]=set(nums)
        longest_Seq: int=0

        for i in nums:
        #check if preceding element exist
            if i-1 not in num_set: 
                current_seq: int=0
                while i+1 in num_set:
                    current_seq +=1
                    i+=1
                longest_Seq= max(current_seq, longest_Seq)
        return longest_Seq