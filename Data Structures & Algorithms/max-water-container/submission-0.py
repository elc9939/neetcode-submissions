class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(a, b):
            return abs(a-b) * min(heights[a],heights[b])
        p1 = 0
        p2 = len(heights) - 1
        best = area(p1, p2)        
        while p2 > p1:
        
            if heights[p1] > heights[p2]:
                p2 -=1
            else:
                p1 +=1
            if area(p1, p2)>best:
                best = area(p1, p2) 
        return best