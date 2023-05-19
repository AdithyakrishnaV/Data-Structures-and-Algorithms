class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: dict[int, int] = {}
        freq: List[List[int]] = [[] for _ in range(len(nums) + 1)]
        result: List[int] = []

        for n in nums:
            count[n] = count.get(n,0) + 1
            # using hashmap to find the frequency 
            #of each occurance
        for val, key in count.items():
            freq[key].append(val)
        for i in range(len(freq) -1,0,-1):
            for n in freq[i]:
                result.append(n)
                if len(result)==k:
                    return result