def reorderLogFiles(logs):
    ll = []
    dl = []
    for each in logs:
        temp = each.split(' ')
        if temp[1].isnumeric():
            dl.append(each)
        else:
            ll.append(each)

    ll.sort(key= lambda a: a.split(' ')[1:] + list(a[0]))

    ll.extend(dl)

    return ll



s =["dig1 8 1 5 1","dig2 3 6","let2 own kit dig","let3 art zero","let1 art can"]

s1 = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]

print (reorderLogFiles (s1))