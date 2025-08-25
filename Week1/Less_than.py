def less_than(original: list, n: int):
    """
    less_than is a function that gets a list input "original" and a number n.
    It returns the list of every element in original less than n.
    """
    less = []
    for num in original:
        if num < n:
            less.append(num)
    return less


print(less_than([4, 1, 3, 2, 5, 0, -2], 2))
print(less_than([], 10))
print(less_than(list(range(20)), 5))

# Test 1
original = [1, 2, 3, 4, 5]
n = 3
result = less_than(original, n)
assert result == [1, 2]

# Test 2
original = [10, 20, 30, 40, 50]
n = 35
result = less_than(original, n)
assert result == [10, 20, 30]

# Test 3
original = [-1, 0, 1, 2, 3]
n = 0
result = less_than(original, n)
assert result == [-1]