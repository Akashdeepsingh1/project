class Classy:
    def __int__(self):
        pass

    def largestMAligned(self, arr, m):
        min_num = min(arr)
        max_num = max(arr)

        final_count = 0
        for i in range(len(arr)):
            count = 1
            for j in range(i+1,len(arr)):
                if (abs(arr[j]) + abs(arr[i]))%m == 0:
                    count+=1

            if final_count < count:
                final_count = count

        return final_count


a = [-3,-2,1,0,8,7,1]
obj = Classy()
print (obj.largestMAligned (a, 3))