class Solution:
    def countBits(self, n: int) -> List[int]:
        curr = 1
        l = [0]
        while curr <= n/2:
            l = l + [i+1 for i in l]
            curr *= 2
        l = l + [l[i]+1 for i in range(n-curr+1)]
        return l