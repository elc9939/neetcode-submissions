class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst = sorted(nums)
        soln = []
        for k in range(len(lst) - 2):
            if k > 0 and lst[k] == lst[k-1]:
                continue
            i = k+1
            j = len(lst) - 1
            while i < j:
                total = lst[i]+lst[j]+lst[k]
                if total == 0:
                    soln.append([lst[k],lst[i],lst[j]])
                    while i < j and lst[i] == lst[i+1]:
                        i += 1
                    while i < j and lst[j] == lst[j-1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif total > 0:
                    j -= 1
                else:
                    i += 1
        return soln


