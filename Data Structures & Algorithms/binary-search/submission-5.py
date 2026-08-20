class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        low = 0
        high = len(nums) - 1
        if nums[low] == target:
            return low
        if nums[high] == target:
            return high
        if nums[low] > target or nums[high] < target:
            return -1

        while low <= high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return -1