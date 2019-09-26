class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return []

        intervals.sort(key = lambda x:x[0])
        start = intervals[0][0]
        finish = intervals[0][1]
        ret = []

        for interval in intervals:
            if interval[0] > finish:
                ret.append([start, finish])
                start = interval[0]
            finish = max(finish, interval[1])

        ret.append([start, finish])
        return ret
        
"""
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
