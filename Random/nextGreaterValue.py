def nextGreater(input_list):
    if not input_list:
        return None
    l = len(input_list)
    for i in range(l):
        temp = input_list[i]
        for j in range(i, l):
            if input_list[i] < input_list[j]:
                input_list[i] = input_list[j]
                break
        if input_list[i] == temp:
            input_list[i] = 0
    return input_list


input_list = [2, 1, 5]
print(nextGreater(input_list))

input_list1 = [2, 7, 4, 3, 5]
print(nextGreater(input_list1))

input_list2 = [1, 7, 5, 1, 9, 2, 5, 1]
print(nextGreater(input_list2))

# approach 2


def nextGreater2(input_list):
    if not input_list:
        return None
    l = len(input_list)
    current_biggest = input_list[-1]
    input_list[-1] = 0
    for i in range(l-2, -1, -1):
        # if input_list[i] <
        pass

    for i in range(l):
        temp = input_list[i]
        for j in range(i, l):
            if input_list[i] < input_list[j]:
                input_list[i] = input_list[j]
                break
        if input_list[i] == temp:
            input_list[i] = 0
    return input_list
