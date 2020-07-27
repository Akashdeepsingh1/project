import heapq
def reorganizeString (S):
    pq = [(-S.count (x), x) for x in set (S)]
    heapq.heapify (pq)
    if any (-nc > (len (S) + 1) / 2 for nc, x in pq):
        return ""

    ans = []
    while len (pq) >= 2:
        nct1, ch1 = heapq.heappop (pq)
        nct2, ch2 = heapq.heappop (pq)
        # This code turns out to be superfluous, but explains what is happening
        # if not ans or ch1 != ans[-1]:
        #    ans.extend([ch1, ch2])
        # else:
        #    ans.extend([ch2, ch1])
        ans.extend ([ch1, ch2])
        if nct1 + 1: heapq.heappush (pq, (nct1 + 1, ch1))
        if nct2 + 1: heapq.heappush (pq, (nct2 + 1, ch2))

    return "".join (ans) + (pq[0][1] if pq else '')


def stringReorganize(s):
    if not s:
        return 0

    from collections import Counter
    import heapq

    d = Counter(s)
    new_d = [(-1*v,k) for k,v in d.items()]
    heapq.heapify(new_d)
    final_s = []
    while len(new_d)>1:
        item1_v , item1_k = heapq.heappop(new_d)
        item2_v, item2_k = heapq.heappop(new_d)

        final_s.append(item1_k)
        final_s.append(item2_k)

        item1_v +=1
        item2_v +=1
        if item1_v != 0 :
            heapq.heappush(new_d,(item1_v,item1_k))
        if item2_v != 0:
            heapq.heappush(new_d,(item2_v,item2_k))

    if len(new_d) == 1:
        final_s.append(heapq.heappop(new_d)[1])

    return ''.join(final_s)


#print (reorganizeString ('aaaabbbbccc'))
print (stringReorganize ('aaaabbbbccc'))