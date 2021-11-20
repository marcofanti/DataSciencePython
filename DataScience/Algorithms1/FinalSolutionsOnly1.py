



def getSortedRank(a):

    len_a = len(a)
    a_marked = []
    r = [0] * (len_a)
    for i in range(len_a):
        a_marked.append((a[i], i))
    #print(a_marked)
    a_marked.sort()
    #print(a_marked)
    for j in range(len_a):
        pos = a_marked[j][1]
        #print('pos ', pos)
        r[pos] = j
        #print(r)
    return r


print(' -- Test 1 -- ')
print('[-1, 5, -2, 3, 0, 2]')
r = getSortedRank([-1, 5, -2, 3, 0, 2])
print(r)



print(' -- Test 2 --')
a1 =[-1, 6, 7, 8, 2, 3, 2, 1, 0, 5, 4, 2]
r1 = getSortedRank(a1)
print(r1)

