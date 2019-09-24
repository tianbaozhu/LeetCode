class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_log = []
        digits_log = []
        for log in logs:
            log = log.split()
            if log[1].isdigit():
                digits_log.append(" ".join(log))
            else:
                letter_log.append((" ".join(log[1:]), "".join(log[0])))

        letter_log.sort(key = lambda x: (x[0], x[1]))
        letter_log = [x[1]+" "+x[0] for x in letter_log]
        
        return letter_log + digits_log

"""
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
"""
