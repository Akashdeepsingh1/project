'''
def scheduler(items, cooldown):
    if not items or len(items) < 2:
        return len(items)
    if cooldown == 0:
        return len(items)

    from collections import defaultdict
    from heapq import heappush, heappop, heapify

    counter = defaultdict(int)
    heap = []

    for i in range(len(items)):
        counter[items[i]] -= 1

    for k, v in counter.items():
        heappush(heap, (v, k))
    final_list = []

    while heap:
        temp_pos = []
        temp_counter = -1
        while temp_counter != cooldown:
            temp_counter += 1
            if not heap:
                if not temp_pos:
                    break
                final_list.append('idle')

            else:
                item = heappop(heap)
                final_list.append(item[1])
                #item[0] += 1
                if item[0] != -1:
                    temp_pos.append((item[0]+1, item[1]))
        if temp_pos:
            heap.extend(temp_pos)
            heapify(heap)
    return len(final_list)


print(scheduler(['A', 'A', 'A', 'B', 'B', 'B'], 4))

tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
n = 2
print(scheduler(tasks, n))

print(scheduler([], 2))

'''
from collections import Counter


class Solution:
    def leastInterval(self, tasks, n):

        if n == 0:
            # Quick response for special case on n = 0
            # no requirement for cooling, just do those jobs in original order
            return len(tasks)

        # key   : task
        # value : occurrence of tasks
        task_occ_dict = Counter(tasks)

        # max occurrence among tasks
        max_occ = max(task_occ_dict.values())

        # number of tasks with max occurrence
        number_of_taks_of_max_occ = sum(
            (1 for task, occ in task_occ_dict.items() if occ == max_occ))

        # Make (max_occ-1) groups, each groups size is (n+1) to meet the requirement of cooling
        # Fill each group with uniform iterleaving as even as possible

        # At last, execute for the last time of max_occ jobs
        intervl_for_schedule = (max_occ-1)*(n+1) + number_of_taks_of_max_occ

        # Minimal length is original length on best case.
        # Otherswise, it need some cooling intervals in the middle
        return max(len(tasks), intervl_for_schedule)


obj = Solution()
#print(obj.leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 3))

tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
n = 2
print(obj.leastInterval(tasks, n))

#print(obj.leastInterval([], 2))
