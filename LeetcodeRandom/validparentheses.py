def isValid ( s):
    """
    :type s: str
    :rtype: bool
    """
    l = []
    para = {']': '[','}':'{',')':'('}
    if len(s) == 0:
        return True
    for each in s:
        le = len(l)
        if each.isalnum() or each == ' ':
            pass
        elif le > 0 :
            if each in para.keys():
                if l[le-1] == para[each]:
                    del l[le-1]

                else:
                    return False
            else:
                l.extend(each)
        else:
            l.extend(each)
    if len(l) == 0:
        return True

print(isValid('{[]}'))