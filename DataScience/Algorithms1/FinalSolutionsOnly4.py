def findCommonSorted(list1, list2):
    # your code here
    n1 = len(list1)
    n2 = len(list2)
    if n1 == 0: # lst1 is empty
        return []
    elif n2 == 0:
        return []
    else:
        output_lst = []  # This is the list we will return
        i1 = 0
        i2 = 0
        while (i1 < n1 and i2 < n2):
            if list1[i1] == list2[i2]:
                output_lst.append(list1[i1])
                i1 = i1 + 1
                i2 = i2 + 1
            else:
                if list1[i1] < list2[i2]:  # lst[i1] is the smaller elt
                    i1 = i1 + 1 # advance index i1
                else:
                    i2 = i2 + 1 # advance index i2
            #print('output_lst ', i1, i2, output_lst)
        return output_lst

print('--Test 1--')
list1 = [ -2, 3, 5, 10, 12,  15, 18]
list2 = [-10, -5, -2, 1, 4, 5, 11, 18]
out12 = findCommonSorted(list1, list2)
print(out12)
assert out12 == [-2, 5, 18]
print('passed')
print('--Test 2--')
list3 = [-1, 0, 2, 5, 7, 19, 22, 26, 29, 32, 36]
list4 = [-10, -4, -2, 0, 5, 7, 12, 18, 20, 21, 25, 29, 36]
out34 = findCommonSorted(list3, list4)
print(out34)
assert out34 == [0, 5, 7, 29, 36]
print('passed')
print('--Test 3--')
list5 = list(range(0, 100,2))
list6 = list(range(1, 101, 2))
out56 = findCommonSorted(list5, list6)
assert len(out56) ==0
print('passed')

print('All tests passed: 5 points!')
