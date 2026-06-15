class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        for elem in s:
            if elem not in d:
                d[elem] = [0,0]
            d[elem][0] += 1
        for elem in t:
            if elem not in d:
                d[elem] = [0,0]
            d[elem][1] += 1
            
        for elem in d:
            if d[elem][0] != d[elem][1]:
                return False
        return True