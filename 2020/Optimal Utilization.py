def solution(a,b, target):
    a.sort(key = lambda x:x[1])
    b.sort(key = lambda x:x[1])

    a_len = len(a)
    b_len = len(b)
    final_list = []
    temp = 0
    temp_list = []
    for i in range(a_len):
        for j in range(b_len):
            if a[i][1] + b[j][1] == target:
                final_list.append([a[i][0],b[j][0]])
            if temp<=a[i][1] + b[j][1]<target:
                if temp == a[i][1] + b[j][1]:
                    temp_list.append([a[i][0],b[j][0]])
                else:
                    temp_list = [[a[i][0],b[j][0]]]
                temp = a[i][1] + b[j][1]
            if temp < a[i][1] + b[j][1]  < target:
                temp_list = [a[i][0],b[j][0]]


    if final_list:
        return final_list
    else:
        return temp_list

import unittest


class Test(unittest.TestCase):

    def test_get_closes_pairs_to_target(self):
        a = [[1, 20], [2, 15], [3, 5]]
        b = [[1, 80], [2, 11], [3, 1]]
        target = 17
        self.assertEqual([[3,2],[2, 3]], solution(a, b, target),
                         "Should return correct list of closes pairs to target when input is unsorted lists")

        a = [[1, 2], [2, 4], [3, 6]]
        b = [[1, 2]]
        target = 7
        self.assertEqual([[2, 1]], solution(a, b, target), "Should return correct list of closes pairs to target")

        a = [[1, 3], [2, 5], [3, 7], [4, 10]]
        b = [[1, 2], [2, 3], [3, 4], [4, 5]]
        target = 10
        self.assertEqual([[2, 4], [3, 2]], solution(a, b, target),
                         "Should return correct list of closes pairs to target")

        a = [[1, 8], [2, 7], [3, 14]]
        b = [[1, 5], [2, 10], [3, 14]]
        target = 20
        self.assertEqual([[3, 1]], solution(a, b, target),
                         "Should return correct list of closes pairs to target")

        a = [[1, 8], [2, 15], [3, 9]]
        b = [[1, 8], [2, 11], [3, 12]]
        target = 20
        self.assertEqual([[1, 3], [3, 2]], solution(a, b, target),
                         "Should return correct list of closes pairs to target")

        a = [[1, -8], [2, 15], [3, -9]]
        b = [[1, 8], [2, -11], [3, -12]]
        target = 1
        self.assertEqual([[1, 1]], solution(a, b, target),
                         "Should return correct list of closes pairs to target when inputs have negative numbers")

        a = []
        b = [[1, 8], [2, 11], [3, 12]]
        target = 20
        self.assertEqual([], solution(a, b, target),
                         "Should return empty list when a is empty list")

        a = [[1, 8], [2, 15], [3, 9]]
        b = []
        target = 20
        self.assertEqual([], solution(a, b, target),
                         "Should return empty list when b is empty list")

        a = []
        b = []
        target = 20
        self.assertEqual([], solution(a, b, target),
                         "Should return empty list when a and b is empty list")




'''

a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10
print (solution (a, b, target))







a = [[1, 20], [2, 15], [3, 5]]
b = [[1, 80], [2, 11], [3, 1]]
target = 17

print(solution(a,b,target))


'''


