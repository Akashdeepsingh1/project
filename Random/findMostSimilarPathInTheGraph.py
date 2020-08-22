
import collections
# to do


def most_similar_path(graph, path):
    queue = collections.deque([('', -1, 0, [])])
    max_sim, best_path = -1, ''

    while len(queue) > 0:
        a, level, sim, p = queue.popleft()

        if level == len(path)-1:
            if sim >= max_sim:
                if sim == max_sim:
                    x = ''.join(p)
                    y = ''.join(best_path)
                    z = ''.join(path)

                    d1 = sum([x[i] == z[i] for i in range(len(z))])
                    d2 = sum([y[i] == z[i] for i in range(len(z))])

                    if d1 > d2:
                        best_path = p
                else:
                    max_sim = sim
                    best_path = p

        else:
            if level == -1:
                if path[level+1] in graph:
                    queue.append(
                        (path[level+1], level+1, sim+1, p + [path[level+1]]))
                else:
                    for x in graph:
                        queue.append((x, level+1, sim, p + [x]))
            else:
                if a in graph:
                    if path[level+1] in graph[a]:
                        queue.append(
                            (path[level+1], level+1, sim+1, p + [path[level+1]]))
                    else:
                        for x in graph[a]:
                            queue.append((x, level+1, sim, p + [x]))
    return best_path


graph = [["ATH", "TBS"], ["TBS", "DME"], ["DME", "LCA"], ["LCA", "TLV"], ["TLV", "ATH"],
         ["ICN", "IKT"], ["IKT", "DME"], ["DME", "LED"],
         ["LED", "SVO"], ["SVO", "BEG"], ["BEG", "TIV"],
         ["SVO", "PRG"], ["LED", "PRG"],
         ["PRG", "DUB"], ["PRG", "MXP"], ["PRG", "ORY"], [
             "PRG", "CRL"], ["PRG", "AMS"],
         ["DME", "AUH"], ["AUH", "CGK"], ["CGK", "DPS"], [
             "DPS", "SIN"], ["SIN", "CGK"],
         ["KUL", "DPS"], ["SIN", "BKK"], ["SIN", "PEK"], ["PEK", "MSQ"], ["MSQ", "LED"]]
most_similar_path(graph, ["AXX", "TBS", "DME"])
