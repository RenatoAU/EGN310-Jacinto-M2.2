"""Correct linear-search and binary-search implementations."""


def linear_search(values: list[int], target: int) -> int:
    """Return the index of target, or -1 when target is not present.

    Linear search does not require the list to be sorted. If a value appears
    more than once, this function returns the first matching index.
    """
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def binary_search(values: list[int], target: int) -> int:
    """Return an index containing target, or -1 when it is not present.

    The input list must be sorted in ascending order. With duplicate values,
    the returned index may be any index containing target.
    """
    left = 0
    right = len(values) - 1

    # <= is important: left and right can point to the same final candidate.
    while left <= right:
        middle = left + (right - left) // 2

        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1
