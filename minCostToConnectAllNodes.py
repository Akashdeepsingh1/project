'''

Given an undirected graph with n nodes labeled 1..n. Some of the nodes are already connected. The i-th edge connects nodes edges[i][0] and edges[i][1] together. Your task is to augment this set of edges with additional edges to connect all the nodes. Find the minimum cost to add new edges between the nodes such that all the nodes are accessible from each other.

Input:

n, an int representing the total number of nodes.
edges, a list of integer pair representing the nodes already connected by an edge.
newEdges, a list where each element is a triplet representing the pair of nodes between which an edge can be added and the cost of addition, respectively (e.g. [1, 2, 5] means to add an edge between node 1 and 2, the cost would be 5).
Example 1:

Input: n = 6, edges = [[1, 4], [4, 5], [2, 3]], newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
Output: 7
Explanation:
There are 3 connected components [1, 4, 5], [2, 3] and [6].
We can connect these components into a single component by connecting node 1 to node 2 and node 1 to node 6 at a minimum cost of 5 + 2 = 7.


'''
from collections import defaultdict
from collections import deque
import heapq
class Solution:
    def __init__(self):
        pass

    def minCostConnect(self,n,  newEdges, edges):
        graph = defaultdict(list)
        possibleedges = set()
        for each in newEdges:
            graph[each[0]].append((each[2],each[1]))
            graph[each[1]].append((each[2],each[0]))
            possibleedges.add((each[0],each[1]))
            possibleedges.add((each[1],each[0]))
        for each in edges:
            if tuple(each) not in possibleedges:
                graph[each[0]].append((0,each[1]))
                graph[each[1]].append((0,each[0]))



        self.visited = []
        rev = 0
        #que = deque((0,1))
        que = [(0,1)]
        heapq.heapify(que)


        while que:
            cost, node = heapq.heappop(que)
            if node not in self.visited:
                print(cost)
                rev+=cost
                self.visited.append(node)
                for new_cost,new_node in graph[node]:
                    if new_node not in self.visited:
                        heapq.heappush(que,(new_cost,new_node))
        if len(self.visited) == n:
            return rev
        else:
            return -1

n = 6
edges = [[1, 4], [4, 5], [2, 3]]
newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]

obj = Solution()
print (obj.minCostConnect (n, newEdges, edges))



