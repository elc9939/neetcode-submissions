class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        lst = sorted(nums)
        lst = [elem for elem in lst if not elem > target]
        for i in range(len(lst)):
            l = lst[0:i+1]
            k = self.combinationSum(l,target - lst[i])
            for elem in k:
                elem.append(lst[i])
                ret.append(elem)
        if target in nums:
            ret.append([target])
        return ret