class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        # time complexity O(n * log(n))
        # space complexity O(1)
        intervals.sort(key=lambda x:x[0])
        end = 0

        for interval in intervals:
            if end > interval[0]:
                return False
            end = interval[1]
            
        return True
