class Classy:
    def __init__(self):
        pass

    def criticalPoints(self,gph,edges):
        '''

        :param graph:
        :return:
        Input: numNodes = 7, numEdges = 7, edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
        '''
        if not gph:
            return []

        from collections import defaultdict,deque
        self.graph = defaultdict(list)
        for each in gph:
            self.graph[each[0]].append(each[1])
            self.graph[each[1]].append(each[0])

        final_list = []
        index = 0
        len_item = len(self.graph.keys())
        print(len_item)
        while index<edges:
            if index == edges-1:
                start = 1
            else:
                start = index +1

            temp_val = self.graph[index]
            self.graph[index] = []
            d = deque()
            d.append(start)
            self.visited = []
            while d:
                curr_item = d.pop()
                if curr_item not in self.visited:
                    d.extend(self.graph[curr_item])
                    self.visited.append(curr_item)
            if len(self.visited) != edges:
                final_list.append(index)
            self.graph[index] = temp_val
            index +=1
        return final_list



edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
obj = Classy()
print (obj.criticalPoints (edges, 7))

edges1 = [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]]
print(obj.criticalPoints(edges1,9))