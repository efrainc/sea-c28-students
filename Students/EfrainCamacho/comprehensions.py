"""List Comprehensions Homework"""


def count_evens(nums):
    """Return the number of even numbers in a list"""


    return len(filter(lambda x: not x % 2, nums))


if __name__ == '__main__':
    assert count_evens([2, 2, 1, 3, 4]) == 3
    assert count_evens([2, 2, 0]) == 3
    assert count_evens([1, 3, 5]) == 0
    print "All Test Passed"
