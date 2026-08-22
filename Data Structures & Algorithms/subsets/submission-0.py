class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        fin = []
        for i in range(2 ** len(nums)):
            lst = []
            n = i
            for j in range(len(nums)):
                if n % 2 == 1:
                    lst.append(nums[j])
                n = n // 2
            fin.append(lst)
        return fin