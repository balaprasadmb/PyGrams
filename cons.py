def check(input1, input2):
    check_num = min(input2)
    len1 = 1
    input2 = list(set(sorted(input2)))
    for i in input2[1:]:
        check_num +=1
        print i, check_num
        if check_num == i:
            len1 += 1
            print 'if:', len1
#         else:
#             len1 = -1
#             check_num = min(input2[input2.index(i):])
#             print 'else:', len1
    if len1 == 1:
        return -1
    else:
        return len1

l = [1,2,3,4,10,20]
l = [1,2,4,10,20]
print check(len(l), l)
