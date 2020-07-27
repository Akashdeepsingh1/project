class Solution:
    def criticalConnections(self, n, connections):
        '''
        :param n: 4
        :param connections:   [[0,1],[1,2],[2,0],[1,3]]
        :return: [[1,3]]
        '''
        from collections import defaultdict, deque

        self.graph = defaultdict(list)
        self.AR = []
        for each in connections:
            self.graph[each[0]].append(each[1])
            self.graph[each[1]].append(each[0])

        for k,v in self.graph.items():
            temp = v
            self.graph[k] = []
            que = deque()
            self.visited = []
            if k+1<n:
                que.append(k+1)
            else:
                que.append(0)
            while que:
                temp = que.pop()
                if temp not in self.visited:
                    self.visited.append(temp)
                    que.extend(self.graph[temp])

            if len(self.visited) != n:
                for each in v:
                    if each not in self.visited and [each,k] not in self.AR and [k,each] not in self.AR:
                        self.AR.append([k,each])
            self.graph[k] = v
        return self.AR

#n = 4
#connections = [[0,1],[1,2],[2,0],[1,3]]

n = 5
connections = [[1,0],[2,0],[3,2],[4,2],[4,3],[3,0],[4,0]]
obj = Solution ()
print (obj.criticalConnections (n, connections))




