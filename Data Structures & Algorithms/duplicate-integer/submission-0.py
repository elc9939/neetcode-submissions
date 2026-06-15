class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        for elem in nums:
            if elem in d:
                return True
            else:
                d[elem] = True
        return False