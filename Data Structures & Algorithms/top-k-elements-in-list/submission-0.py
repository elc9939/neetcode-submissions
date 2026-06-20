class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        d = {}
        for elem in nums:
            d[elem] = d.get(elem, 0) + 1
        for key, value in d.items():
            buckets[value].append(key)
        i=0
        b=len(nums) - 1
        lst = []
        while i < k:
            for elem in buckets[b]:
                lst.append(elem)
                i+=1
            b-=1
        return lst