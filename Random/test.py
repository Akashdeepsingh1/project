count = 0
m = 3
n = 3
k = 5
num = 12
for val in range(1, m + 1):  # count row by row
    add = min(num // val, n)
    if add == 0:  # early exit
        break
    count += add
if count >= k:
    print(count)
