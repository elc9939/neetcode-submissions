class Solution:
    def findMin(self, nums: List[int]) -> int:
        small = 0
        big = len(nums) - 1
        while big-small>=2:
            medium = (small + big) // 2
            if nums[big]-nums[medium]>0:
                big = medium
            else:
                small = medium
        return min(nums[small], nums[big])