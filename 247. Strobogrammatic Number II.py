class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # time complexity O(5 ^ (n/2))
        # space complexity O(n)
        self.set1 = ["0","1","8"]
        self.set2 = [("0","0"),("1","1"),("6","9"),("9","6"),("8","8")]
        if n == 1:
            return self.set1
        if n == 2:
            return [x+y for x,y in self.set2[1:]]
        self.ret = []

        def dfs(curr, length):
            if length == 0:
                self.ret.append(curr)
                return
            else:
                for x,y in self.set2:
                    if x == "0" and y == "0" and length == 2:
                        continue
                    dfs(x+curr+y, length-2)

        if n%2 == 0:
            dfs("", n)
        else:
            for ch in self.set1:
                dfs(ch, n-1)

        return self.ret
