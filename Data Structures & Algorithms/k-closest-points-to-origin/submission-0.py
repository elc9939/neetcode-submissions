class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return (x**2 + y**2) ** 0.5
        d = []
        for i in range(len(points)):
            d.append([points[i], dist(points[i][0], points[i][1])])
        d.sort(key = lambda x:x[1])
        lst = [d[i][0] for i in range(k)]
        return lst