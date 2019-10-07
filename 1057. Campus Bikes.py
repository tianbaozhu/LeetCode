class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        # time complexity O(mnlog(mn))
        # space complexity O(mn)
        pairs = []
        visited_worker = set()
        visited_bike = set()
        count = 0
        ret = [0 for x in range(len(workers))]
        for i in range(len(workers)):
            for j in range(len(bikes)):
                pairs.append((abs(workers[i][0]-bikes[j][0])+abs(workers[i][1]-bikes[j][1]), i, j))
        for pair in sorted(pairs):
            dis, worker, bike = pair[0],pair[1],pair[2]
            if worker not in visited_worker and bike not in visited_bike:
                visited_worker.add(worker)
                visited_bike.add(bike)
                ret[worker] = bike
                count += 1
                if count == len(workers):
                    break
        return ret
