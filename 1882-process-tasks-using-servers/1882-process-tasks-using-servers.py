class Solution(object):
    def assignTasks(self, servers, tasks):
        n = len(servers)
        m = len(tasks)

        freeServers = []

        busyServers = []

        for i in range(n):
            heapq.heappush(freeServers, (servers[i], i))

        result = [0] * m

        for i in range(m):

            while busyServers and busyServers[0][0] <= i:
                finishTime, weight, index = heapq.heappop(busyServers)

                heapq.heappush(freeServers, (weight, index))

            if not freeServers:
                finishTime, weight, index = heapq.heappop(busyServers)
                startTime = finishTime

            else:
                weight, index = heapq.heappop(freeServers)
                startTime = i

            result[i] = index

            heapq.heappush(
                busyServers,
                (startTime + tasks[i], weight, index)
            )

        return result