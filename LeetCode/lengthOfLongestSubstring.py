class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sSet: Set[T] = set()
        l: int = 0
        result: int = 0

        for r in range(len(s)):
            while s[r] in sSet:
                sSet.remove(s[l])
                l += 1
            sSet.add(s[r])
            result = max(result, r-l+1)
        return result