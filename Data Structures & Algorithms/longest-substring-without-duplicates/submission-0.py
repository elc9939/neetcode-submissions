class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = 0
        b = 0
        d = {}
        m = 0
        curr = 0
        while b < len(s):
            if d.get(s[b], 0) == 0:
                d[s[b]] = 1
                b += 1
                curr += 1
                if curr > m:
                    m = curr
            else:
                while s[a] != s[b] and a < b:
                    d[s[a]] = 0
                    a += 1
                    curr -= 1
                d[s[a]] = 1
                a += 1
                curr -= 1
                
                d[s[b]] = 1
                b += 1
                curr += 1
        return m
                