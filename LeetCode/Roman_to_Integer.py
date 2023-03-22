class Solution():
    def romanToInt(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        roman: dict[str, int] = { 'I': 1, 
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000 }
        
        sol=0
        for a,b in zip(s,s[1:]):
            if roman[a]<roman[b]:
                sol -=roman[a]
            else:
                sol +=roman[a]
        return sol + roman[s[-1]]