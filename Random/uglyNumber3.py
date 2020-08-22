import math


def nthUglyNumber(n: int, a: int, b: int, c: int) -> int:
    def enough(num) -> bool:
        mod_a = mid//a
        mod_b = mid//b
        mod_c = mid//c
        mod_ab = mid//ab
        mod_ac = mid//ac
        mod_bc = mid//bc
        mod_abc = mid//abc
        total = mid//a + mid//b + mid//c - mid//ab - mid//ac - mid//bc + mid//abc
        return total >= n

    ab = a * b // math.gcd(a, b)
    ac = a * c // math.gcd(a, c)
    bc = b * c // math.gcd(b, c)
    abc = a * bc // math.gcd(a, bc)
    left, right = 1, 10
    while left < right:
        mid = left + (right - left) // 2
        if enough(mid):
            right = mid
        else:
            left = mid + 1
    return left


print(nthUglyNumber(3, 2, 3, 5))
