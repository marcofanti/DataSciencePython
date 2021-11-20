def findAllCommonElementsSorted(list_of_lists):
    assert len(list_of_lists) >= 2
    # your code here
    len_lists = len(list_of_lists)
    len_li = [0] * len_lists
    index_i = [0] * len_lists

    for i in range(len_lists):
        len_li[i] = len(list_of_lists[i])
        #print('len[i] ', i, len_li[i])
        if len_li == 0: # lst i is empty
            #print('list ', i, ' is empty')
            return []

    output_lst = []  # This is the list we will return

    are_we_done = False
    while not are_we_done:
        # Test if they are all the same
        areEqual = True
        for i in range(len_lists - 1):
            elem_i = list_of_lists[i][index_i[i]]
            elem_iplus1 = list_of_lists[i + 1][index_i[i + 1]]
            #print('i', i)
            #print('elem_i', elem_i)
            #print('elem_iplus1', elem_iplus1)
            if elem_i != elem_iplus1:
                areEqual = False
                break
        if areEqual:
            output_lst.append(elem_i)
            #print('******  appending ', elem_i)
            for i in range(len_lists):
                index_i[i] += 1
        else:
            min_elem = list_of_lists[0][index_i[0]]
            min_elem_list = 0
            for i in range(len_lists):
                elem = list_of_lists[i][index_i[i]]

                if elem <= min_elem:
                    min_elem = elem
                    min_elem_list = i

            #print ('incrementing index_i[min_elem_list] for list ', min_elem_list, index_i[min_elem_list])
            index_i[min_elem_list] += 1
            #print ('index_i[min_elem_list]  ', index_i[min_elem_list])

        for i in range(len_lists):
            if index_i[i] >= len_li[i]:
                #print('index_i[i] >= len_li[i]', index_i[i], len_li[i])
                are_we_done = True
                break

    return output_lst

print(' -- Test 1 --')
list1 = [ [-3, 1, 3, 4, 5, 8], [-8, 2, 2, 3, 4, 5, 10] ]
out1 = findAllCommonElementsSorted(list1)
print(out1)
assert(out1 == [3, 4, 5])
print('passed')
print(' -- Test 2 --')
list2 = [ [1, 3, 5], [4, 5, 7], [1,  5, 8], [-4, 3, 5], [1, 1, 5], [1, 5, 5] ]
out2 = findAllCommonElementsSorted(list2)
print(out2)
assert len(out2)== 1
assert 5 in out2
print('passed')

print('-- Test 3 --')
list3 = [[ -5, -2, -1, 1, 4], [-3, -2, -2,  1, 1, 2, 4, 5, 6], [-2, 1, 3, 4, 5, 6, 7, 8]]
out3 = findAllCommonElementsSorted(list3)
print(out3)
assert out3 == [-2, 1, 4]
print('passed')
print('-- Test 4 --')
list4 = [ [1, 2, 2, 3, 4,  6,  6, 7,  7], [3, 4, 8, 8, 9, 9], [0, 1, 4, 8, 12,18,  56, 67], [0, 0, 0, 1, 1, 3, 5, 6,  7, 8]]
out4= findAllCommonElementsSorted(list4)
print(out4)
assert len(out4) == 0
print('All Tests Passed: 5 points')
