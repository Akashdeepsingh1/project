def climbStairs (n: int) -> int:
        def _helper (n):
            if n in d:
                return d[n]
            return _helper (n - 1) + _helper (n - 2)

        from collections import defaultdict
        d = defaultdict(int)
        d[0] = 0
        d[1] = 1
        d[2] = 2
        d[3] = 3
        for i in range(n+1):
            d[i] = _helper(i)

        return d[n]


print (climbStairs (44))