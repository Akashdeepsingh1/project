def openLock(target, deadends):
    if target in deadends or '0000' in deadends:
        return -1
    from collections import deque
    q = deque([('0000', 0)])
    final_step = float('inf')
    visited = []

    while q:
        item = q.popleft()
        curr, step = item[0], item[1]

        if curr == target:
            if final_step > step:
                print(curr)
                final_step = step
        elif final_step < step:
            continue
        else:
            for i in range(4):
                prv = curr[:i] + str((int(curr[i]) - 1) % 10) + curr[i+1:]
                nxt = curr[:i] + str((int(curr[i]) + 1) % 10) + curr[i+1:]

                if prv not in deadends or prv not in visited:
                    q.append([prv, step+1])

                if nxt not in deadends or prv not in visited:
                    q.append([nxt, step+1])

                visited.extend([prv, nxt])

    print(final_step)


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"

print(openLock(target, deadends))
