class Classy:
    def __init__(self):
        pass

    def longestTurbutetnArray(self, A):
        '''

        :param A:
        :return:
        A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:
        For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
        OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
        That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

        Return the length of a maximum size turbulent subarray of A.



        Example 1:

        Input: [9,4,2,10,7,8,8,1,9]
        Output: 5
        Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
        Example 2:

        Input: [4,8,12,16]
        Output: 2
        Example 3:

        Input: [100]
        Output: 1
        '''

        if not A:
            return 0
        elif len(A) <= 2:
            return len(A)
        else:
            count_odd = 0
            count_even = 0
            for i in range(len(A)-1):
                if i%2 == 1 and A[i] > A[i+1]:
                    count_odd+=1
                if i%2 == 0 and A[i]<A[i+1]:
                    count_odd+=1
                if i % 2 == 0 and A[i] > A[i + 1]:
                    count_even += 1
                if i % 2 == 1 and A[i] < A[i + 1]:
                    count_even+=1
            return max(count_even,count_odd)

    def NumberGreaterThanPosition(self,A):

        for i in range(len(A)):
            count = 0
            for j in range(i+1,len(A)):
                if A[j]>i:
                    count+=1
            A[i] = count
        return A


obj = Classy()
A = [9,4,2,10,7,8,8,1,9]
print (obj.longestTurbutetnArray (A))

print(obj.NumberGreaterThanPosition(A))