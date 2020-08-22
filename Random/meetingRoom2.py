def meetingRoom(schedule):
    from heapq import heappush, heappop
    rooms = []

    sorted(schedule)
    # schedule.sort(schedule[0])

    for each in schedule:
        if len(rooms) == 0:
            heappush(rooms, each[1])
        else:
            existing_item = heappop(rooms)
            new_item_st = each[0]
            new_item_et = each[1]

            if existing_item > new_item_st:
                heappush(rooms, existing_item)
                heappush(rooms, new_item_et)
            else:
                # heappush(rooms,existing_item)
                heappush(rooms, new_item_et)
    return len(rooms)


rooms = [0, 30], [5, 10], [15, 20]
print(meetingRoom(rooms))


'''
    [0,30], [5,10], [5,30], [15,20], [30,40]


 * we will insert the end time in the heap 
 * each time we iterate we will check the top most element of the heap 
 and see if it is greater or lesser than the smallest element of the heap
      
 taking the max count      
rooms = [30]
mc = 1
iteration 2

rooms_endTime = [10,30]
mc = 2
iteration 3

check 10(poped element) > or < 5(new element start time)
rooms = [10,30,30]
mc = 3
iteration 4
15 < or > 10

rooms = [20,30,30]
mc = 3

iteration 5

20 < or > 30 
2 ways 
1. rooms = [20,30,30, 40]
mc = 4
[31,50]
rooms = [31,40]
mc = 
[30,30,31,40]





either we can pop out all the elements of the heap till the start time of the new element is 
greater equal  then the elements in the heap
[30,40]

2. 




'''
