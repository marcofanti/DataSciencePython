
def returnAllCommonElements(list_of_lists):
    a_dict = {}
    common_elem = []
    len_lists = len(list_of_lists)

    for i in range(len_lists):
        len_list = len(list_of_lists[i])
        for j in range(len_list):
            elem = list_of_lists[i][j]
            #print('elem ', elem)
            if i == 0:
                if elem not in a_dict:
                    a_dict[elem] = 1
                    #print('Adding to level 0 ', elem)
            else:
                if elem in a_dict:
                    print(f'a_dict[{elem}] = {a_dict[elem]}')
                    if a_dict[elem] < i + 1:
                        a_dict[elem] += 1
        # finished with 1 list, i remove all elements with value < i + 1
        if i > 0:
            print('i, j = ', i, j)
            for key in a_dict:
                if a_dict[key] < (i + 1):
                    a_dict[key] = -1000;

        print(' a_dict ', a_dict)
    for key in a_dict:
        if a_dict[key] >= len_lists:
            print(key, '->', a_dict[key])
            common_elem.append(key)
    return common_elem

print(' -- Test 1 --')
list1 = [ [ 1, 5, 8, -3, 4, 1, 3], [2, 5, 10, -8, 4, 3, 2] ]
out1 = returnAllCommonElements(list1)
print(out1)
assert len(out1) == 3
assert 5 in out1
assert 4 in out1
assert 3 in out1
print('passed')
print(' -- Test 2 --')
list2 = [ [1, 3, 5], [5, 4, 7], [8, 1, 5], [-4, 3, 5], [1, 1, 5], [1, 5, 5] ]
out2 = returnAllCommonElements(list2)
print(out2)
assert len(out2)== 1
assert 5 in out2
print('passed')

print('-- Test 3 --')
list3 = [[1, -5, 4, -2, -1], [2, -3, 1, -2, 4, 6, 1, 5, -2], [4, 5, 6, 7, 8, 1, 3, -2]]
out3 = returnAllCommonElements(list3)
print(out3)
assert len(out3) == 3
assert 1 in out3
assert 4 in out3
assert -2 in out3
print('passed')
print('-- Test 4 --')
list4 = [ [1, 2, 4, 7, 2, 6, 3, 6, 7], [8, 9,  3, 4, 8, 9], [1, 4, 56, 12, 67, 8, 0, 18], [0, 1, 7, 8, 0, 1, 3, 5, 6, 0, 19]]
out4= returnAllCommonElements(list4)
print(out4)
assert len(out4) == 0

print('All Tests Passed: 15 points')
