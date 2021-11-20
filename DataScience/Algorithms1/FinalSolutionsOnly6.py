
def findMinContainingInterval(a1, a2):
    # Assume a1, a2 are sorted
    # Return a tuple (lo, hi) of the interval.
    assert len(a1) > 0
    assert len(a2) > 0
    n1 = len(a1)
    n2 = len(a2)
    i = -1
    j = -1
    smallest_interval = 10000000000000
    i1 = 0
    i2 = 0
    while (i1 < n1 and i2 < n2):
        if a1[i1] < a2[i2]:
            if (a2[i2] - a1[i1]) < smallest_interval:
                smallest_interval = a2[i2] - a1[i1]
                i = i1
                j = i2
                #print('smallest_interval a', smallest_interval, i1, i2)
            i1 = i1 + 1
        else:
            if (a1[i1] - a2[i2]) < smallest_interval:
                smallest_interval = a1[i1] - a2[i2]
                i = i1
                j = i2
                #print('smallest_interval b', smallest_interval, i1, i2)
            i2 = i2 + 1
    if a1[i] < a2[j]:
        return a1[i], a2[j]
    else:
        return a2[j], a1[i]

from random import randint

def arrayHasEltInInterval(a, l, u):
    assert l <= u
    for elt in a:
        if l <= elt and elt <= u:
            return True
    return False

print('-- Test 1 --')
a1 = [ 1, 4, 8, 9, 14, 15, 18 ]
a2 = [ 5, 10,  19, 23]
(l, u) = findMinContainingInterval(a1, a2)
print(l, u)
assert u -l == 1
assert arrayHasEltInInterval(a1, l, u)
assert arrayHasEltInInterval(a2, l, u)
print('passed')

print('-- Test 2 --')
a1 = [1, 5, 10, 11, 18, 21, 28, 37]
a2 = [ -4, 16, 34, 32]
(l, u) =  findMinContainingInterval(a1, a2)
print(l, u)
assert u - l == 2
assert arrayHasEltInInterval(a1, l, u)
assert arrayHasEltInInterval(a2, l, u)
print('passed')

print('-- Test 3 -- ')
a1 = list(range(0, 100000, 5))
a2 = list(range(257, 1000000, 7))
(l, u) =  findMinContainingInterval(a1, a2)
print(l, u)
assert u - l == 0
assert arrayHasEltInInterval(a1, l, u)
assert arrayHasEltInInterval(a2, l, u)
print('passed')

print('-- Test 4--')
a1 = sorted([ randint(-1000000, 1000000) for i in range(100000)])
a2 = sorted([ randint(0, 1000) for i in range(100)])
(l, u) =  findMinContainingInterval(a1, a2)
print(l, u)
assert arrayHasEltInInterval(a1, l, u)
assert arrayHasEltInInterval(a2, l, u)

print('All Tests Passed: 10 points.')

