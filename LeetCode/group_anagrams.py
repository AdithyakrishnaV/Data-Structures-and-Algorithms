class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res: defaultdict[list]=defaultdict(list)

        for word in strs:
            count=[0] * 26 #a-z

            for char in word:

                count[ord(char) - ord("a")] +=1 #KEY

            res[tuple(count)].append(word)
            #converts the list to a tuple, and uses it as
            #a key to store the words in the res dictionary
        return res.values()