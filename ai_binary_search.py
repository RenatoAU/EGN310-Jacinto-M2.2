"""Binary search returned by the AI assistant for defect hunting.

This version is intentionally kept unchanged so that the edge-case test can
demonstrate the defect found during review.
"""


def binary_search_ai(values: list[int], target: int) -> int:
    """Return the index of target, or -1 when target is not found."""
    left = 0
    right = len(values) - 1

    while left < right:
        middle = (left + right) // 2

        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1
