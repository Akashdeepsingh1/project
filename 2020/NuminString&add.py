def add2Num(num1, num2):

    # create 2 list of the number

    l1 = list (num1)
    l2 = list (num2)

    # put the numbers in the stack
    # keeping poping each number and maintain a carry then after addtion push it down to third stack
    from collections import deque
    d = deque()
    carry = 0
    while l1 and l2:
        temp1 = int(l1.pop())
        temp2 = int(l2.pop())

        temp_sum= temp1+temp2+ carry

        carry = temp_sum//10
        d.appendleft(str(temp_sum%10))

    while l1:
        temp1 = int(l1.pop())
        temp_sum = temp1+carry
        carry = temp_sum//10
        d.appendleft(str(temp_sum%10))

    while l2:
        temp1 = int(l2.pop())
        temp_sum = temp1+carry
        carry = temp_sum//10
        d.appendleft(str(temp_sum%10))
    if carry >0:
        d.appendleft(str(carry))


    # keeping poping element from the third stack and multiple the old sum * 10 and add the poped element

    return ''.join(d)


print (add2Num ('536', '1049'))
