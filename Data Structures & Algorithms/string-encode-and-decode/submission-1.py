class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for elem in strs:
            n = len(elem)
            s = s + str(n//100) + str((n%100)//10) + str(n%10) + elem
        return s
            


    def decode(self, s: str) -> List[str]:
        i = 0
        lst = []
        while i < len(s):
            count = int(s[i:i+3])
            i += 3
            lst.append(s[i:i+count])
            i += count
        return lst