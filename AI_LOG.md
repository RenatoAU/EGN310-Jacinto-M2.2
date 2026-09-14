# AI Log — Search Implementation and Defect Hunt

## Prompt sent to the AI assistant

> Write a beginner-friendly Python binary-search function named
> `binary_search_ai(values, target)`. The input list is sorted in ascending
> order. Return the index of the target if it is found; otherwise return `-1`.
> Do not use Python's built-in `index` method. Include only the function and
> keep the explanation short.

## AI-generated implementation used for testing

The assistant returned this implementation, which was saved in
`ai_binary_search.py`:

```python
def binary_search_ai(values: list[int], target: int) -> int:
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
```

## My review

I reviewed the loop condition and tested an edge case with one element. The
implementation works for some ordinary inputs, but it skips the final
candidate when `left == right`. I kept the code unchanged in order to submit
the failing test required by the assignment. The corrected implementation is
in `search.py`.

## Independent verification

The test in `tests/test_ai_binary_search_defect.py` uses `[42]` and target
`42`. The expected result is index `0`, but the AI function returns `-1`.
The correct implementation uses `while left <= right`, so it checks the final
candidate and passes the equivalent single-element test.
