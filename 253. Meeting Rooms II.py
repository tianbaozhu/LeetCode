class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x:x[0])
        ret = 1
        priority_queue = []
        heapq.heappush(priority_queue, intervals[0][1])

        for interval in intervals[1:]:
            while len(priority_queue) > 0 and interval[0] >= priority_queue[0]:
                heapq.heappop(priority_queue)
            heapq.heappush(priority_queue, interval[1])
            ret = max(ret, len(priority_queue))

        return ret
        
"""
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Input: [[7,10],[2,4]]
Output: 1
"""
