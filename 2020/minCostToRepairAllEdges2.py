from collections import defaultdict

class solution:
    def __init__(self):
        pass

    def minCost(self, edgesToRepair,edges):
        addedEdges = set()
        graph = defaultdict (list)
        for each in edgesToRepair:
            graph[each[0]].append((each[2],each[1]))
            graph[each[1]].append((each[2],each[0]))
            addedEdges.add((each[0],each[1]))
            addedEdges.add((each[0],each[1]))

        for each in edges:
            if each not in addedEdges:
                graph[each[0]].append((0,each[1]))
                graph[each[1]].append((0,each[0]))

        self.visited = []
        queue = [(0,1)]
        rev = 0
        import heapq
        heapq.heapify(queue)
        while queue:
            cost, node = queue.pop()
            if node not in self.visited:
                self.visited.append(node)
                rev += cost
                for cost,node in graph[node]:
                    if node not in self.visited:
                        heapq.heappop(queue,(cost,node))

        return rev



