class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr = 1
        a = []
        b = []
        for elem in nums:
            
            a.append(curr)
            curr *= elem
        curr = 1
        for i in range(len(nums)):
            
            b.append(curr)
            curr *= nums[len(nums) - 1 - i]
        return[b[len(nums) - i -1] * a[i] for i in range(len(nums))]
