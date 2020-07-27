from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def minimumCost (self, N: int, connections) -> int:
        from collections import defaultdict
        graph = defaultdict (list)
        edges = set ()

        for each in connections:
            graph[each[0]].append ((each[2], each[1]))
            graph[each[1]].append ((each[2], each[0]))
            edges.add ((each[0], each[1]))
            edges.add ((each[1], each[0]))

        self.visited = []
        import heapq
        queue = [(0, 1)]
        heapq.heapify (queue)
        rev = 0

        while queue:
            cost, node = heapq.heappop(queue)
            if node not in self.visited:
                rev += cost
                self.visited.append (node)
                for cost, connectedNode in graph[node]:
                    if connectedNode not in self.visited:
                        heapq.heappush (queue, (cost, connectedNode))
        if len (self.visited) == N:
            return rev
        else:
            return -1


    def minimumCost2(self, edges, connection):

        self.graph2 = defaultdict(list)

        for i in range(len(connection)):
            self.graph2[connection[i][0]].append([connection[i][2], connection[i][1]])
            self.graph2[connection[i][1]].append([connection[i][2],connection[i][0]])

        self.visited = []
        heap = [[0,1]]
        res = 0
        while heap:
            cost, city = heappop(heap)
            if city not in self.visited:
                res += cost
                self.visited.append(city)
                for each in self.graph2[city]:
                    heappush(heap,[each[0],each[1]])
        if len(self.visited) == edges:
            return res
        else:
            return -1

n = 3
connection = [[1,2,5],[1,3,6],[2,3,1]]
obj = Solution()
print (obj.minimumCost2 (n, connection))