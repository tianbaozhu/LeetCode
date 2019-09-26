class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if len(points) <= K:
            return points
        if len(points) == 0 or K == 0:
            return []
        left = 0
        right = len(points)-1
        pivot = self.quickselect(left, right, points)
        while pivot != K-1:
            if pivot < K:
                left = pivot + 1
                pivot = self.quickselect(left, right, points)
            else:
                right = pivot - 1
                pivot = self.quickselect(left, right, points)

        return points[:K]

    def distance(self, point):
        return point[0]**2 + point[1]**2

    def quickselect(self, left, right, points):
        while left < right:
            if self.distance(points[left]) <= self.distance(points[right]):
                left += 1
            else:
                points[left], points[right-1] = points[right-1], points[left]
                points[right], points[right-1] = points[right-1], points[right]
                right -= 1
        return right

"""
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
"""
