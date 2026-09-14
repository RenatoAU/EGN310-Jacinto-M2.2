# Defect Report

## Failing test

```python
def test_ai_binary_search_finds_target_in_single_element_list():
    assert binary_search_ai([42], 42) == 0
```

## Explanation

The AI-generated binary search has a boundary-condition defect because it uses `while left < right` instead of `while left <= right`. For the input `[42]` and target `42`, both boundaries start at index `0`, so `left < right` is false and the loop never checks the only element; the function incorrectly returns `-1` instead of `0`. The same problem can occur whenever the target is the final remaining candidate. The corrected `binary_search` in `search.py` uses `<=`, which allows that last candidate to be examined.
